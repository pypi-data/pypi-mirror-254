from __future__ import annotations

from importlib import import_module

import spacy

from errant.annotator import Annotator
from errant.utils import get_spacy_models_for_language

# ERRANT version
__version__ = 'v1.0.0rc04'


# Load an ERRANT Annotator object for a given language
def load(lang='en', model_name='en_core_web_sm', nlp=None):
    # Make sure the language is supported
    supported = {'en'}
    if lang not in supported:
        raise Exception('%s is an unsupported or unknown language' % lang)

    model_names = get_spacy_models_for_language(lang)
    if model_name not in model_names:
        spacy.cli.download(model_name)

    # Load spacy
    nlp = nlp or spacy.load(model_name, disable=['ner'])

    # Load language edit merger
    merger = import_module('errant.en.merger')

    # Load language edit classifier
    classifier = import_module('errant.en.classifier')
    # The English classifier needs spacy
    if lang == 'en':
        classifier.nlp = nlp

    # Return a configured ERRANT annotator
    return Annotator(lang, nlp, merger, classifier)
