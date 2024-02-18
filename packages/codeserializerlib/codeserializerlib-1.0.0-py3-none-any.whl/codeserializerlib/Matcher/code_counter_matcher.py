import spacy
from spacy.matcher import Matcher
from spacy.tokens import Span
from spacy.util import compile_infix_regex
import os
from enum import Enum
from Models.Labels import Label


@Language.component("code_counter_matcher")
def code_counter_matcher(nlp):
    matcher = init_matcher(nlp)

    def matcher_pipe(doc):
        matches = matcher(doc)
        for match_id, start, end in matches:
            matched_span = doc[start:end]
            middle_index = None
            for i, token in enumerate(matched_span):
                if token.lower_ in ["*", "x", "mal"]:
                    middle_index = i
                    break

            if middle_index is not None:
                code_count = Span(doc, start, start + middle_index, label=Label.code_count.value)
                credit_amount = Span(doc, start + middle_index + 1, end, label=Label.credit_amount.value)
            else:
                code_count = Span(doc, start, end, label=Label.code_count.value)
                credit_amount = Span(doc, start, end, label=Label.credit_amount.value)

            new_ents = [e for e in doc.ents if not (start <= e.start < end or start < e.end <= end)]
            new_ents += [code_count, credit_amount]
            doc.ents = new_ents

        return doc

    return matcher_pipe


def init_matcher(nlp):
    # Get default infixes and add 'x' to them
    infixes = list(nlp.Defaults.infixes) + [r"(?<=[0-9])x(?=[0-9€])"]

    # Update infixes in tokenizer
    nlp.tokenizer.infix_finditer = compile_infix_regex(infixes).finditer

    # Initialize the Matcher
    matcher = Matcher(nlp.vocab)

    # Define the pattern
    pattern = [
        {"LIKE_NUM": True},  # Matches tokens that represent numbers
        {"LOWER": {"IN": ["*", "x", "mal"]}},  # Matches tokens
        {"LIKE_NUM": True},  # Matches tokens that represent numbers
        {"IS_CURRENCY": True}  # Matches tokens that represent currency symbols
    ]

    # Add the pattern to the matcher
    matcher.add("NUM_MULTIPLICATION", [pattern])

    return matcher
