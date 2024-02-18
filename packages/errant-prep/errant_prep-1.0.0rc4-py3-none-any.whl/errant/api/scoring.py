import errant
from typing import Any
from collections import Counter
from errant.utils import merge_dict, computeFScore, get_results, convert_errant_to_prep_result
import re

annotator = errant.load(lang="en", model_name="en_core_web_sm")


def get_edits(orig: str, edit: str, coder: int = 0) -> list:
    orig = annotator.parse(orig)
    edit = annotator.parse(edit)
    edits = annotator.annotate(orig, edit)
    return [[e.o_start, e.o_end, e.type, e.c_str, coder] for e in edits]

def get_list_edit(edits, coder):
    
    edits_ = []
    for edit in edits:
        start = edit.start
        end = edit.end
        correction = edit.correction
        type_error = edit.operator + ":" + edit.type_error
        edits_.append([start, end, type_error, correction, coder])
    return edits_
        
def process_edits(edits, dt=False, ds=False, single=False, multi=False, filt=None, cse=False):
    coder_dict = {}

    # Add an explicit noop edit if there are no edits.
    if not edits:
        edits = [[-1, -1, 'noop', '-NONE-', 0]]

    # Loop through the edits
    for edit in edits:
        start, end, cat, cor, coder = edit

        # Add the coder to the coder_dict if necessary
        coder_dict.setdefault(coder, {})

        # Apply filters
        if cat == 'UNK' and not dt and not ds:
            continue
        if single and (end - start >= 2 or len(cor.split()) >= 2):
            continue
        if multi and end - start < 2 and len(cor.split()) < 2:
            continue
        if filt and cat in filt:
            continue

        # Token Based Detection
        if dt:
            process_token_based_detection(coder_dict, coder, start, end, cat)

        # Span Based Detection
        elif ds:
            process_span_based_detection(coder_dict, coder, start, end, cat)

        # Span Based Correction
        else:
            process_span_based_correction(coder_dict, coder, start, end, cat, cor, cse)

    return coder_dict

def process_token_based_detection(coder_dict, coder, start, end, cat):
    if start == -1:
        coder_dict[coder].setdefault((start, start), []).append(cat)
    elif start == end and start >= 0:
        coder_dict[coder].setdefault((start, start + 1), []).append(cat)
    else:
        for tok_id in range(start, end):
            coder_dict[coder].setdefault((tok_id, tok_id + 1), []).append(cat)

def process_span_based_detection(coder_dict, coder, start, end, cat):
    coder_dict[coder].setdefault((start, end), []).append(cat)

def process_span_based_correction(coder_dict, coder, start, end, cat, cor, cse):
    key = (start, end, cat, cor) if cse else (start, end, cor)
    coder_dict[coder].setdefault(key, []).append(cat)

def evaluate_edits(hyp_dict, ref_dict, best, beta=0.5):

    # Initialize best scores
    best_tp, best_fp, best_fn, best_f = 0, 0, 0, -1
    best_hyp, best_ref = 0, 0
    best_cat = {}

    # Compare each hyp and ref combination
    for hyp_id, hyp_edits in hyp_dict.items():
        for ref_id, ref_edits in ref_dict.items():
            # Get the local counts for the current combination.
            tp, fp, fn, cat_dict = compareEdits(hyp_edits, ref_edits)

            # Compute the local sentence scores (for verbose output only)
            loc_p, loc_r, loc_f = computeFScore(tp, fp, fn, beta)

            # Compute the global sentence scores
            p, r, f = computeFScore(tp + best['tp'], fp + best['fp'], fn + best['fn'], beta)

            # Check if the current scores are better than the best scores
            if (f, tp, -fp, -fn) > (best_f, best_tp, -best_fp, -best_fn):
                best_tp, best_fp, best_fn = tp, fp, fn
                best_f, best_hyp, best_ref = f, hyp_id, ref_id
                best_cat = cat_dict

    # Save the best TP, FP, and FNs as a dict, and return this and the best_cat dict
    best_dict = {'tp': best_tp, 'fp': best_fp, 'fn': best_fn}
    return best_dict, best_cat

def compareEdits(hyp_edits, ref_edits):
    tp = 0  # True Positives
    fp = 0  # False Positives
    fn = 0  # False Negatives
    cat_dict = {}  # {cat: [tp, fp, fn], ...}

    for h_edit, h_cats in hyp_edits.items():
        # noop hyp edits cannot be TP or FP
        if h_cats[0] == 'noop':
            continue
        # TRUE POSITIVES
        if h_edit in ref_edits.keys():
            # On occasion, multiple tokens at same span.
            for h_cat in ref_edits[h_edit]:  # Use ref dict for TP
                tp += 1
                # Each dict value [TP, FP, FN]
                if h_cat in cat_dict.keys():
                    cat_dict[h_cat][0] += 1
                else:
                    cat_dict[h_cat] = [1, 0, 0]
        # FALSE POSITIVES
        else:
            # On occasion, multiple tokens at same span.
            for h_cat in h_cats:
                fp += 1
                # Each dict value [TP, FP, FN]
                if h_cat in cat_dict.keys():
                    cat_dict[h_cat][1] += 1
                else:
                    cat_dict[h_cat] = [0, 1, 0]
    for r_edit, r_cats in ref_edits.items():
        # noop ref edits cannot be FN
        if r_cats[0] == 'noop':
            continue
        # FALSE NEGATIVES
        if r_edit not in hyp_edits.keys():
            # On occasion, multiple tokens at same span.
            for r_cat in r_cats:
                fn += 1
                # Each dict value [TP, FP, FN]
                if r_cat in cat_dict.keys():
                    cat_dict[r_cat][2] += 1
                else:
                    cat_dict[r_cat] = [0, 0, 1]
    return tp, fp, fn, cat_dict

def merge_edits_to_text(orig_text, edits):
    # Sort edits based on start index and then by priority in descending order
    sorted_edits = sorted(edits, key=lambda x: (x.start, -x.priority))
    
    merged_text = ""
    last_end = 0
    
    for edit in sorted_edits:
        # If the current edit starts before the last one ended, skip it
        if edit.start < last_end:
            continue
        
        # Add the text from the last edit's end to the current edit's start
        merged_text += orig_text[last_end:edit.start]
        
        # Add the correction of the current edit
        if edit.operator == "R":
            merged_text += edit.correction
            last_end = edit.end
        elif edit.operator == "U":
            last_end = edit.end
        elif edit.operator == "M":
            merged_text += edit.correction
            last_end = edit.end - 1
    
    # Add any remaining text from the original text
    merged_text += orig_text[last_end:]

    merged_text = re.sub("\s+", " ", merged_text)
    
    return merged_text

def convert_pairs_to_list_edits(orig, target, coder=0):
    orig = annotator.parse(orig)
    target = annotator.parse(target)
    edits = annotator.annotate(orig, target)
    result = []
    for e in edits:
        result.append(
            [e.o_start, e.o_end, e.type, e.c_str, coder]
        )
    return result

def get_scores(
        eval_data: list,
        cat: int = 2,
        beta: float=0.5,
        coder: int = 0
):

    best_dict = Counter({'tp': 0, 'fp': 0, 'fn': 0})
    best_cats = {}

    for data in eval_data:
        # Simplify the edits into lists of lists
        orig = data.original_text
        hyp_edits = data.pred_edits
        ref_edits = data.true_edits

        pred = merge_edits_to_text(
            orig_text=orig,
            edits=hyp_edits
        )
        refr = merge_edits_to_text(
            orig_text=orig,
            edits=ref_edits
        )

        hyp_edits = convert_pairs_to_list_edits(orig, pred, coder)
        ref_edits = convert_pairs_to_list_edits(orig, refr, coder)

        # hyp_edits = get_list_edit(hyp_edits, coder)
        # ref_edits = get_list_edit(ref_edits, coder)
        # Process the edits for detection/correction based on args
        hyp_dict = process_edits(hyp_edits)
        ref_dict = process_edits(ref_edits)
        # Evaluate edits and get best TP, FP, FN hyp+ref combo.
        count_dict, cat_dict = evaluate_edits(
            hyp_dict, ref_dict, best_dict
        )
        # Merge these dicts with best_dict and best_cats
        best_dict += Counter(count_dict)
        best_cats = merge_dict(best_cats, cat_dict)

    result_dng = get_results(best_dict, best_cats, cat=cat, beta=beta)
    best_dict_prep, best_cats_prep = convert_errant_to_prep_result(
        best_dict, best_cats,
    )
    result_prep = get_results(best_dict_prep, best_cats_prep, cat=cat, beta=beta)

    for k, v in result_dng.items():
        if 'Marco Avg' == k:
            continue
        else:
            result_dng[k].append(v[0] + v[2])
    
    result_dng['Marco Avg'].append(result_dng['Micro Avg'][-1])

    for k, v in result_prep.items():
        if 'Marco Avg' == k:
            continue
        else:
            result_prep[k].append(v[0] + v[2])
    
    result_prep['Marco Avg'].append(result_prep['Micro Avg'][-1])
    

    return result_dng, result_prep

