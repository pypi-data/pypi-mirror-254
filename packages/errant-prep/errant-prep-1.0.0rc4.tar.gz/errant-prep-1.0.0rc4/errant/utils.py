from __future__ import annotations

import spacy

from errant.constants import MAPPING_ERRANT_ACA

from errant.helper import calculate_mean


def get_available_spacy_models() -> list[str]:
    """
    Get a list of available spaCy models installed in the current environment.

    Returns:
        List[Text]: A list of available spaCy model names.
    """
    installed_models = spacy.info().get('pipelines', '')
    if not installed_models:
        return []
    return list(installed_models.keys())


def get_spacy_models_for_language(lang: str) -> list[str]:
    """
    Get a list of spaCy models that support a specific language.

    Args:
        lang (Text): The language code (e.g., 'en' for English) to filter models by.

    Returns:
        List[Text]: A list of spaCy model names that support the specified language.
    """
    installed_models = get_available_spacy_models()
    if not installed_models:
        return []

    return [
        model_name
        for model_name in installed_models
        if model_name.split('_')[0] == lang
    ]


def convert_errant_to_prep_result(best_dict, best_cats):
    result = {}
    for error_cat, value in best_cats.items():
        tp, fp, fn = value[0], value[1], value[2]

        type_error = error_cat[2:]
        opra_error = error_cat[:2]

        type_error = MAPPING_ERRANT_ACA[type_error]
        error_cat = opra_error + type_error
        if error_cat not in result:
            result[error_cat] = [0, 0, 0]
        result[error_cat][0] += tp
        result[error_cat][1] += fp
        result[error_cat][2] += fn

    return best_dict, result

def merge_dict(dict1, dict2):
    for cat, stats in dict2.items():
        if cat in dict1.keys():
            dict1[cat] = [x + y for x, y in zip(dict1[cat], stats)]
        else:
            dict1[cat] = stats
    return dict1

def print_results(best, best_cats, dt=False, ds=False, cse=False, cat=1, beta=1):
    # Prepare output title.
    title = ''
    if dt:
        title = ' Token-Based Detection '
    elif ds:
        title = ' Span-Based Detection '
    elif cse:
        title = ' Span-Based Correction + Classification '
    else:
        title = ' Span-Based Correction '

    result = {}

    # Category Scores
    if cat:
        best_cats = processCategories(best_cats, cat)
        print('')
        print(f'{title:=^66}')
        print(
            'Category'.ljust(14),
            'TP'.ljust(8),
            'FP'.ljust(8),
            'FN'.ljust(8),
            'P'.ljust(8),
            'R'.ljust(8),
            'F' + str(beta),
        )
        for cat, cnts in sorted(best_cats.items()):
            cat_p, cat_r, cat_f = computeFScore(cnts[0], cnts[1], cnts[2], beta)
            print(
                cat.ljust(14),
                str(cnts[0]).ljust(8),
                str(cnts[1]).ljust(8),
                str(cnts[2]).ljust(8),
                str(cat_p).ljust(8),
                str(cat_r).ljust(8),
                cat_f,
            )

            result[cat] = [cnts[0], cnts[1], cnts[2], cat_p, cat_r, cat_f]

        mic_p = calculate_mean([s[3] for s in result.values()])
        mic_r = calculate_mean([s[4] for s in result.values()])
        mic_f = calculate_mean([s[5] for s in result.values()])

        result['Marco Avg'] = [
            None, None, None, round(mic_p, 4), round(mic_r, 4), round(mic_f, 4),
        ]

        mac_p, mac_r, mac_f = computeFScore(best['tp'], best['fp'], best['fn'], beta)
        result['Micro Avg'] = [
            best['tp'], best['fp'], best['fn'], mac_p, mac_r, mac_f,
        ]

    # Print the overall results.
    print('')
    print(f'{title:=^46}')
    print('\t'.join(['TP', 'FP', 'FN', 'Prec', 'Rec', 'F' + str(beta)]))
    print(
        '\t'.join(
            map(
                str,
                [best['tp'], best['fp'], best['fn']] +
                list(computeFScore(best['tp'], best['fp'], best['fn'], beta)),
            ),
        ),
    )
    print('{:=^46}'.format(''))
    print('')

def get_results(best, best_cats, dt=False, ds=False, cse=False, cat=1, beta=1):
    # Prepare output title.
    title = ''
    if dt:
        title = ' Token-Based Detection '
    elif ds:
        title = ' Span-Based Detection '
    elif cse:
        title = ' Span-Based Correction + Classification '
    else:
        title = ' Span-Based Correction '

    result = {}

    # Category Scores
    if cat:
        best_cats = processCategories(best_cats, cat)
        for cat, cnts in sorted(best_cats.items()):
            cat_p, cat_r, cat_f = computeFScore(cnts[0], cnts[1], cnts[2], beta)

            result[cat] = [cnts[0], cnts[1], cnts[2], cat_p, cat_r, cat_f]

        mic_p = calculate_mean([s[3] for s in result.values()])
        mic_r = calculate_mean([s[4] for s in result.values()])
        mic_f = calculate_mean([s[5] for s in result.values()])

        result['Marco Avg'] = [
            None, None, None, round(mic_p, 4), round(mic_r, 4), round(mic_f, 4),
        ]

        mac_p, mac_r, mac_f = computeFScore(best['tp'], best['fp'], best['fn'], beta)
        result['Micro Avg'] = [
            best['tp'], best['fp'], best['fn'], mac_p, mac_r, mac_f,
        ]
    return result


def computeFScore(tp, fp, fn, beta):
    p = float(tp) / (tp + fp) if fp else 1.0
    r = float(tp) / (tp + fn) if fn else 1.0
    f = float((1 + (beta**2)) * p * r) / \
        (((beta**2) * p) + r) if p + r else 0.0
    return round(p, 4), round(r, 4), round(f, 4)

def processCategories(cat_dict, setting):
    # Otherwise, do some processing.
    proc_cat_dict = {}
    for cat, cnt in cat_dict.items():
        if cat == 'UNK':
            proc_cat_dict[cat] = cnt
            continue
        # M, U, R or UNK combined only.
        if setting == 1:
            if cat[0] in proc_cat_dict.keys():
                proc_cat_dict[cat[0]] = [
                    x + y for x, y in zip(proc_cat_dict[cat[0]], cnt)
                ]
            else:
                proc_cat_dict[cat[0]] = cnt
        # Everything without M, U or R.
        elif setting == 2:
            if cat[2:] in proc_cat_dict.keys():
                proc_cat_dict[cat[2:]] = [
                    x + y for x, y in zip(proc_cat_dict[cat[2:]], cnt)
                ]
            else:
                proc_cat_dict[cat[2:]] = cnt
        # All error category combinations
        else:
            return cat_dict
    return proc_cat_dict
