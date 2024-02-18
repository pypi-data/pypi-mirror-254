from spacy.tokens import Doc

from errant.alignment import Alignment
from errant.edit import Edit


from errant.constants import MAPPING_TYPE_ERROR



# Main ERRANT Annotator class
class Annotator:
    # Input 1: A string language id: e.g. "en"
    # Input 2: A spacy processing object for the language
    # Input 3: A merging module for the language
    # Input 4: A classifier module for the language
    def __init__(self, lang, nlp=None, merger=None, classifier=None):
        self.lang = lang
        self.nlp = nlp
        self.merger = merger
        self.classifier = classifier

    # Input 1: A text string
    # Input 2: A flag for word tokenisation
    # Output: The input string parsed by spacy
    def parse(self, text, tokenise=False):
        if tokenise:
            text = self.nlp(text)
        else:
            text = Doc(self.nlp.vocab, text.split())
            # self.nlp.tagger(text)
            # self.nlp.parser(text)
            text = self.nlp(text)
        return text

    # Input 1: An original text string parsed by spacy
    # Input 2: A corrected text string parsed by spacy
    # Input 3: A flag for standard Levenshtein alignment
    # Output: An Alignment object
    def align(self, orig, cor, lev=False):
        return Alignment(orig, cor, lev)

    # Input 1: An Alignment object
    # Input 2: A flag for merging strategy
    # Output: A list of Edit objects
    def merge(self, alignment, merging="rules"):
        # rules: Rule-based merging
        if merging == "rules":
            edits = self.merger.get_rule_edits(alignment)
        # all-split: Don't merge anything
        elif merging == "all-split":
            edits = alignment.get_all_split_edits()
        # all-merge: Merge all adjacent non-match ops
        elif merging == "all-merge":
            edits = alignment.get_all_merge_edits()
        # all-equal: Merge all edits of the same operation type
        elif merging == "all-equal":
            edits = alignment.get_all_equal_edits()
        # Unknown
        else:
            raise Exception(
                "Unknown merging strategy. Choose from: "
                "rules, all-split, all-merge, all-equal."
            )
        return edits

    # Input: An Edit object
    # Output: The same Edit object with an updated error type
    def classify(self, edit):
        return self.classifier.classify(edit)

    # Input 1: An original text string parsed by spacy
    # Input 2: A corrected text string parsed by spacy
    # Input 3: A flag for standard Levenshtein alignment
    # Input 4: A flag for merging strategy
    # Output: A list of automatically extracted, typed Edit objects
    def annotate(self, orig, cor, lev=False, merging="rules"):
        alignment = self.align(orig, cor, lev)
        edits = self.merge(alignment, merging)
        for edit in edits:
            edit = self.classify(edit)
        return edits
    
    # Input 1: An original text string
    # Input 2: A corrected text string
    # Input 3: A flag for standard Levenshtein alignment
    # Input 4: A flag for merging strategy
    # Output: A list of automatically extracted, typed Edit objects    
    def annotate_raw_text(self, original_text: str, corrected_text: str, lev=False, merging="rules"):
        
        # doc_orig, _ = self.preprocess(original_text)

        doc_lower_orig, normalized_orig_text = self.preprocess(original_text, lowercase=False)

        # doc_corr, _ = self.preprocess(corrected_text)

        _, normalized_corr_text = self.preprocess(corrected_text, lowercase=False)

        processed_text = self.parse(normalized_orig_text)
        corrected_text = self.parse(normalized_corr_text)
        alignment = self.align(processed_text, corrected_text, lev)
        edits = self.merge(alignment, merging)
        for edit in edits:
            edit = self.classify(edit)
            start_token = edit.o_start
            end_token = edit.o_end
            
            count_idx = 0
            add_space = 0
            for token in doc_lower_orig:
                if token.is_space:
                    add_space += 1
                    continue
                else:
                    if count_idx == start_token:
                        break
                    else:
                        count_idx += 1

            orig_tokens = doc_lower_orig[start_token+add_space:end_token+add_space]
            edit.o_toks.start_char = orig_tokens.start_char
            edit.o_toks.end_char = orig_tokens.end_char

            # edit.c_str = doc_corr[edit.c_start:edit.c_end].text

        edits = self._revise_edits(original_text, processed_text, edits)
        
        return edits
    
    @staticmethod
    def _revise_edits(
        orig: str, normalized_orig: str, edits: list[Edit]
    ) -> list[Edit]:
        """
        Revise edits to match the format expected by the evaluator.
        Args:
            edits: list of edits
            type_error_mapping: mapping of type_error
        Returns:
            revised edits
        """
        for edit in edits:
            operator = edit.type[0]
            type_error = edit.type[2:]
            type_error = MAPPING_TYPE_ERROR[type_error]

            edit.type = operator + ":" + type_error

            if operator == "M":
                if edit.o_toks.start_char == 0:
                    edit.o_toks.end_char = edit.o_toks.start_char
                    edit.c_str = edit.c_str + " "
                else:
                    edit.o_toks.end_char = edit.o_toks.start_char - 1
                if type_error == "PUNCTUATION" and edit.o_toks.start_char != len(
                    orig
                ):
                    edit.o_toks.start_char = edit.o_toks.start_char - 1
                elif type_error == "PUNCTUATION" and edit.o_toks.start_char == len(orig):
                    edit.o_toks.end_char = edit.o_toks.start_char
            elif operator == "U":
                if type_error != "PUNCTUATION":
                    edit.o_toks.end_char = edit.o_toks.end_char + 1
        return edits


    def preprocess(self, text: str, lowercase: bool = False):
        if lowercase:
            text = text.lower()

        doc = self.nlp(text)
        tokens = [token.text for token in doc if not token.is_space]
        return doc, " ".join(tokens)

    # Input 1: An original text string parsed by spacy
    # Input 2: A corrected text string parsed by spacy
    # Input 3: A token span edit list; [o_start, o_end, c_start, c_end, (cat)]
    # Input 4: A flag for gold edit minimisation; e.g. [a b -> a c] = [b -> c]
    # Input 5: A flag to preserve the old error category (i.e. turn off classifier)
    # Output: An Edit object
    def import_edit(self, orig, cor, edit, min=True, old_cat=False):
        # Undefined error type
        if len(edit) == 4:
            edit = Edit(orig, cor, edit)
        # Existing error type
        elif len(edit) == 5:
            edit = Edit(orig, cor, edit[:4], edit[4])
        # Unknown edit format
        else:
            raise Exception(
                "Edit not of the form: " "[o_start, o_end, c_start, c_end, (cat)]"
            )
        # Minimise edit
        if min:
            edit = edit.minimise()
        # Classify edit
        if not old_cat:
            edit = self.classify(edit)
        return edit
