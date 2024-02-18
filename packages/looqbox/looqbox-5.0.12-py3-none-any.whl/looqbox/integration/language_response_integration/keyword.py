from multimethod import multimethod

from looqbox.integration.language_response_integration.language_parser import LanguageParser
from looqbox.objects.response_parameters.keyword.keyword import Keyword
from looqbox.utils.utils import as_dict_ignore_nones


def extract_keyword_values(keyword, only_value, as_dict, default=None):
    """Auxiliary function to extract values from a keyword."""
    if only_value:
        return keyword.values if keyword is not None and isinstance(keyword, Keyword) else default
    if as_dict:
        return [as_dict_ignore_nones(keyword.to_token())] if keyword and isinstance(keyword, Keyword) else None
    return keyword


@multimethod
def get_keyword(keyword: str, par_json, keyword_default=None, only_value=False, as_dict=True) -> Keyword:
    """
    Function to search for a specific keyword inside the JSON sent by the parser

    :param keyword: keyword to be found
    :param par_json: JSON from parser
    :param keyword_default: Default value to be returned
    :param only_value: if True will only return the keyword value
    :return: A Map structure or a single value
    """
    language_parser = LanguageParser()
    extracted_keyword = language_parser.get_asked_keywords(keyword, keyword_default)
    return extract_keyword_values(extracted_keyword, only_value, as_dict, keyword_default)


@multimethod
def get_keyword(keywords: list, par_json, keyword_default=None, only_value=False, as_dict=True):
    """
    Overloaded function to handle multiple keywords.
    """
    return [get_keyword(kw, par_json, keyword_default, only_value, as_dict) for kw in keywords]

