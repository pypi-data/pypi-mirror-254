import base64
import datetime
import importlib.util
import itertools
import json
import os
import random
import re
import string
import types
from dataclasses import asdict
from typing import TextIO

from multimethod import multimethod
from monthdelta import monthdelta

from looqbox.global_calling import GlobalCalling
from looqbox.integration.looqbox_global import Looqbox
from looqbox.objects.response_parameters.condition.temporal_relation import TemporalRelation
from looqbox.utils.i18n.internationalization_manager import I18nManager
from looqbox.utils.quote_formatter import QuoteFormatter

__all__ = ["random_hash", "base64_encode", "base64_decode", "paste_if", "format", "format_cnpj", "format_cpf",
           "title_with_date", "map", "drill_if", "current_day", "partition", "library", "create_i18n_vocabulary",
           "read_response_json", "flatten", "open_file", "as_dict_ignore_nones", "load_json_from_path"]

# Calling global variable
if GlobalCalling.looq.home is None:
    GlobalCalling.set_looq_attributes(Looqbox())


def library(file=None):
    """
    Call (import) functions from a file in the Looqbox server. The file must be in the R folder.

    The return of this function must be saved in a variable to be used like a python module.

    Args:
        file (str): File's name
    
    Returns:
        A module with all the functions from the file
    """
    home = GlobalCalling.looq.home
    config = os.path.join(home, "R")
    name = file.split(".")[0]

    spec = importlib.util.spec_from_file_location(name, os.path.join(config, file))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def random_hash(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for pos in range(size))


def base64_encode(text):
    encoded_text = base64.b64encode(text.encode('utf-8')).decode('utf-8')

    return encoded_text


def base64_decode(text):
    decoded_text = base64.b64decode(text).decode('utf-8')

    return decoded_text


def paste_if(head, args=None, closure="", args_separator="|"):
    """
    Paste only if argument exists, otherwise returns None.

    Args:
        head (str): Text to be inserted before the argument
        args (Any): Value to be inserted after the head, if the value is None, the title will not be shown
        closure (str): Text to be inserted after the argument
        args_separator (str): Character string to separate the results
    
    Returns:
        A string
    
    Examples:
        >>> query = f"SELECT * FROM table WHERE 1 = 1 {paste_if('AND column = ', column_value)}"
    """
    if isinstance(args, dict):
        raise Exception("Dictionary not accept in paste_if")
    elif isinstance(args, list):
        args_with_sep = ""

        for arg in args[0:len(args) - 1]:
            args_with_sep = args_with_sep + str(arg) + args_separator

        return head + args_with_sep + str(args[-1]) + closure

    elif isinstance(args, str):
        return head + args + closure

    elif isinstance(args, float) or isinstance(args, int) or isinstance(args, complex):
        return head + str(args) + closure
    else:
        return ""


def format(value, value_format=None, language=GlobalCalling.looq.language):
    """
    Sets a value according to the specified format.

    For number and percent format, it's necessary to define how many decimal places will be used, since those types does
    haven't a default value. On the other hand, for currency format, one might define a specific symbol or leave it for
    the default value, which is set based on the user's language.

    Args:
        value (any): Value to be formatted
        value_format (str): Format to be assigned to value. Formats allowed:
            * number:<decimal places>
            * percent:<decimal places>
            * currency
            * currency:<Symbol>
            * date
            * datetime
        language (str): Language to be used in the format. Default is the user's language
    
    Returns:
        A string formatted according to the value_format parameter

    Examples:
        >>> format(1.146558649, "number:1") = "1.1"
        >>> format(1.146558649, "number:5") = "1.14656"

        >>> format(0.754624594, "percent:0") = "75%"
        >>> format(0.754624594, "percent:7") = "75,4624594%"

        >>> format(42,27756, "currency:¥") = ¥42,28
        >>> format(42,27756, "currency") = $42,28

        >>> format("2022-01-15", "date") = "01/15/2022" or "15/01/2022" (defined by user's settings in appearance menu, the
        >>> same is applied for "datetime" format)
    """

    if value_format is None:
        # warnings.warn("Format not defined")
        return value

    if isinstance(value_format, types.FunctionType):
        return value_format(value)

    if "number" in value_format:
        value = _format_number(value, value_format)
    elif "percent" in value_format:
        value = _format_percent(value, value_format)
    elif "currency" in value_format:
        value = _format_currency(value, value_format)
    elif value_format == "Date" or value_format == "date":
        value = _format_date(value, date_format=GlobalCalling.looq.date_format)
    elif value_format == "Datetime" or value_format == "datetime":
        value = _format_datetime(value, date_format=GlobalCalling.looq.datetime_format)

    return value


def _format_number(value: float, number_format: str) -> str:
    decimal_size = _get_decimal_format(number_format)
    value_format = "{0:,." + str(decimal_size) + "f}"
    value = value_format.format(float(value))

    if GlobalCalling.looq.decimal_separator == ",":
        value = value.translate(str.maketrans(",.", ".,"))

    return value


def _format_percent(value: float, percent_format: str) -> str:
    decimal_size = _get_decimal_format(percent_format)
    value_format = "{0:,." + str(decimal_size) + "%}"
    value = value_format.format(float(value))

    if GlobalCalling.looq.decimal_separator == ",":
        value = value.translate(str.maketrans(",.", ".,"))

    return value


def _get_decimal_format(value_format: str) -> int:
    number_pattern = "(?<=:)\\d"
    decimal = re.findall(number_pattern, value_format)[0]

    return decimal


def _get_currency_symbol(current_format: str, language=GlobalCalling.looq.language) -> str:
    currency_symbols_options = {
        'pt-br': 'R$',
        'en-us': '$'
    }

    currency_symbol = current_format.split(":")[1] if ":" in current_format else None

    return currency_symbol or currency_symbols_options.get(language, "$")


def _format_currency(value: float, currency_format: str) -> str:
    currency_symbol = _get_currency_symbol(currency_format)

    # Since it's most common to monetary values use 2 decimal places, this format will be fixed for the time being
    formatted_value = _format_number(value, "number:2")

    return f'{currency_symbol}{formatted_value}'


def _format_date(value, date_format=GlobalCalling.looq.date_format):
    if isinstance(value, str):
        value = datetime.datetime.strptime(value, '%Y-%m-%d')

    date_format = _get_date_template(date_format)
    value = datetime.datetime.strftime(value, date_format)
    return value


def _format_datetime(value, date_format=GlobalCalling.looq.date_format):
    if isinstance(value, str):
        value = datetime.datetime.strptime(value, '%Y-%m-%d %H:%M:%S')

    datetime_format = _get_date_template(date_format) + " %H:%M:%S"
    value = datetime.datetime.strftime(value, datetime_format)

    return value


def _get_date_template(date_format):
    template_options = {"dd/mm/yyyy": "%d/%m/%Y",
                        "mm/dd/yyyy": "%m/%d/%Y"}

    date_template = template_options.get(date_format, "%d/%m/%Y")

    return date_template


def format_cnpj(cnpj_string):
    """
    Formats CNPJ to standard format.

    Args:
        cnpj_string (str): Unformatted CNPJ
    
    Returns:
        A string in the CNPJ format XX.XXX.XXX/XXXX-XX
    
    Examples:
        >>> format_cnpj("12345678901234") = "12.345.678/9012-34"
    """
    if not isinstance(cnpj_string, str):
        return ""

    if len(cnpj_string) == 13:
        cnpj_string = '0' + cnpj_string
    elif len(cnpj_string) > 14:
        raise Exception('Invalid CNPJ string: More than 14 digits')

    return cnpj_string[:2] + "." + cnpj_string[2:5] + "." + cnpj_string[5:8] + "/" + \
        cnpj_string[8:12] + '-' + cnpj_string[12:]


def format_cpf(cpf_string):
    """
    Formats CPF to standard format.

    Args:
        cpf_string (str): Unformatted CPF
    
    Returns:
        A string in the CPF format XXX.XXX.XXX-XX
    
    Examples:
        >>> format_cpf("12345678901") = "123.456.789-01"
    """
    return cpf_string[:3] + "." + cpf_string[3:6] + "." + cpf_string[6:9] + '-' + cpf_string[9:]


def week_name(date, language=GlobalCalling.looq.language):
    if language == "pt-br":
        week_rule = ["seg", "ter", "qua", "qui", "sex", "sab", "dom"]
    elif language == "en-us":
        week_rule = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    elif language == "it":
        week_rule = ["lun", "mar", "mer", "gio", "ven", "sab", "do"]

    date_week_day = date.timetuple()[6]

    return week_rule[date_week_day]


def date_range_name(date_int, language=GlobalCalling.looq.language):
    initial_date = date_int[0]
    finish_date = date_int[1]

    date_range = None

    # Case Day
    if initial_date == finish_date:
        if language == "pt-br":
            date_range = week_name(initial_date, language) + " sem: " + str(initial_date.isocalendar()[1]) + "/" \
                         + str(initial_date.year)
        elif language == "en-us":
            date_range = week_name(initial_date, language) + " week: " + str(initial_date.isocalendar()[1]) + "/" \
                         + str(initial_date.year)
        elif language == "it":
            date_range = week_name(initial_date, language) + " week: " + str(initial_date.isocalendar()[1]) + "/" \
                         + str(initial_date.year)

    # Case Week
    if initial_date.timetuple()[6] == 0 and initial_date + datetime.timedelta(days=6) == finish_date:
        if language == "pt-br":
            date_range = "sem: " + str(initial_date.isocalendar()[1]) + " - " + str(initial_date.year)
        elif language == "en-us":
            date_range = "week: " + str(initial_date.isocalendar()[1]) + " - " + str(initial_date.year)
        elif language == "it":
            date_range = "week: " + str(initial_date.isocalendar()[1]) + " - " + str(initial_date.year)

    # Case Month
    if initial_date.day == 1 and initial_date + monthdelta(1) - datetime.timedelta(days=1) == finish_date:
        if language == "pt-br":
            date_range = "mês: " + str(initial_date.month) + "/" + str(initial_date.year)
        elif language == "en-us":
            date_range = "month: " + str(initial_date.month) + "/" + str(initial_date.year)
        elif language == "it":
            date_range = "mese: " + str(initial_date.month) + "/" + str(initial_date.year)

    # Case MTD
    if initial_date.day == 1 and initial_date.month == finish_date.month and datetime.datetime.now().strftime(
            "%Y-%m-%d") == finish_date:
        if language == "pt-br":
            date_range = "mtd: " + str(initial_date.month) + "/" + str(initial_date.year)
        elif language == "en-us":
            date_range = "mtd: " + str(initial_date.month) + "/" + str(initial_date.year)
        elif language == "it":
            date_range = "mtd: " + str(initial_date.month) + "/" + str(initial_date.year)

    # Case Year
    if initial_date.day == 1 and initial_date.month == 1 \
            and initial_date + monthdelta(12) - datetime.timedelta(1) == finish_date:
        if language == "pt-br":
            date_range = "ano: " + str(initial_date.year)
        elif language == "en-us":
            date_range = "year: " + str(initial_date.year)
        elif language == "it":
            date_range = "ieri: " + str(initial_date.year)

    if date_range is None:
        return ""
    else:
        return " (" + date_range + ")"


def validate_datetime(date_text):
    if isinstance(date_text, datetime.datetime):
        return True
    else:
        try:
            datetime.datetime.strptime(date_text, '%Y-%m-%d %H:%M:%S')
            return True
        except ValueError:
            return False


def get_language_mapping(language):
    language = language.lower()
    language_map = {
        "pt-br": {
            "var_day": " dia ",
            "var_from": " de ",
            "var_to": " a ",
            "period_start": "a partir de",
            "period_end": "até",
            "language_source": "pt-br"
        },
        "en-us": {
            "var_day": " day ",
            "var_from": " from ",
            "var_to": " to ",
            "period_start": "from",
            "period_end": "until",
            "language_source": "en-us"
        },
        "it": {
            "var_day": " gio ",
            "var_from": " dal ",
            "var_to": " al ",
            "language_source": "it"
        },
        "pt_br": {
            "var_day": " dia ",
            "var_from": " de ",
            "var_to": " a ",
            "period_start": "a partir de",
            "period_end": "até",
            "language_source": "pt-br"
        },
        "en_us": {
            "var_day": " day ",
            "var_from": " from ",
            "var_to": " to ",
            "period_start": "from",
            "period_end": "until",
            "language_source": "en-us"
        }
    }

    if language not in language_map:
        raise Exception(f"Language {language} is invalid")

    return language_map[language]


def determine_format_type(date_str):
    return "Datetime" if validate_datetime(date_str) else "Date"


def format_single_date(header, date_str, language):
    format_type = determine_format_type(date_str)
    format_type = format_type.lower()
    # TODO get date format from user info
    date_mask = "%Y-%m-%d %H:%M:%S" if format_type == "datetime" else "%Y-%m-%d"
    formatted_date = format(date_str, format_type, language)
    date_as_object = datetime.datetime.strptime(date_str, date_mask)
    return header + language["var_day"] + formatted_date + date_range_name([date_as_object, date_as_object],
                                                                           language.get("language_source",
                                                                                        GlobalCalling.looq.language))


def format_date_range(header, start_date, end_date, language):
    start_format_type = determine_format_type(start_date)
    end_format_type = determine_format_type(end_date)
    formatted_start_date = format(start_date, start_format_type.lower(), language)
    formatted_end_date = format(end_date, end_format_type.lower(), language)

    date_mask_start = "%Y-%m-%d %H:%M:%S" if start_format_type.lower() == "datetime" else "%Y-%m-%d"
    start_date_as_object = datetime.datetime.strptime(start_date, date_mask_start)

    date_mask_end = "%Y-%m-%d %H:%M:%S" if start_format_type.lower() == "datetime" else "%Y-%m-%d"
    end_date_as_object = datetime.datetime.strptime(end_date, date_mask_end)

    return header + language["var_from"] + formatted_start_date + language["var_to"] + formatted_end_date \
        + date_range_name([start_date_as_object, end_date_as_object],
                          language.get("language_source", GlobalCalling.looq.language))


@multimethod
def title_with_date(header: str = None, date_int: list = None, language: str = GlobalCalling.looq.language):
    # Handle None dates

    language_vars = get_language_mapping(language)

    if date_int is None:
        return ""

    if _period_does_not_have_start_date(date_int):
        return header + f" {language_vars['period_end']} " + format(date_int[1],
                                                                    determine_format_type(date_int[1]).lower(),
                                                                    language_vars)
    if _period_does_not_have_end_date(date_int):
        return header + f" {language_vars['period_start']} " + format(date_int[0],
                                                                      determine_format_type(date_int[0]).lower(),
                                                                      language_vars)

    if _period_have_single_date(date_int):
        return format_single_date(header, date_int[0], language_vars)
    else:
        return format_date_range(header, date_int[0], date_int[1], language_vars)


def _period_does_not_have_start_date(date: list[str]) -> bool:
    return date[0] is None


def _period_does_not_have_end_date(date: list[str]) -> bool:
    return date[1] is None


def _period_have_single_date(date) -> bool:
    return date[0] == date[1]


@multimethod
def title_with_date(header: str, date_int: TemporalRelation, language: str = GlobalCalling.looq.language):
    distinct_date = list(sorted(date_int.date_with_evaluated_boundaries))

    return title_with_date(header, distinct_date, language=language)


def map(function_arg, *args):
    """
    Apply function with the arguments defined.

    :param function_arg: Function to apply
    :param args: Function arguments
    :return: The output of the function
    """
    # Verify if it has arguments
    if len(args) == 1 and args[0] is None:
        return function_arg(None)

    # Transforming Nones into str to find the cartesian product
    args_list = list(args)
    for i in range(len(args_list)):
        if args_list[i] is None:
            args_list[i] = ["None"]
    args = tuple(args_list)

    # Finding the cartesian product of my *args
    args_possibilities_list = list(itertools.product(*args))

    # Transform tuple into list
    args_possibilities_list = [list(possibility) for possibility in args_possibilities_list]

    # Turning str None into None type again
    for poss_list in args_possibilities_list:
        for i in range(len(poss_list)):
            if poss_list[i] == "None":
                poss_list[i] = None

    # args_possibilities_list = [args_possibilities_list]

    # Dynamically sending all the possibilities to the function
    result = [function_arg(*arg_product) for arg_product in args_possibilities_list]

    return result


def drill_if(value_link, arg):
    """
    Removes drill in case the correspondent arg is not None.

    Args:
        value_link (list): value_link of the column of row
        arg (Any): Arguments to be evaluated
    
    Returns:
        A list with the value_link without the drill
    """

    if not isinstance(arg, list):
        arg = [arg]

    if len(value_link) == len(list(filter(None, arg))) \
            or (not isinstance(value_link, list) and len(list(filter(None, arg))) == 1):
        value_link = None
    else:
        for i in range(len(arg), 0, -1):
            if arg[i - 1] is not None:
                value_link.remove(value_link[i - 1])

    return value_link


def current_day(format='date'):
    """
    Creates list with current day.

    Args:
        format (str): Format of the date output (date or datetime). Default is date
    
    Returns:
        A list with two elements of the current day.

    Examples:
        >>> current_day(format='date') = ["2020-01-01", "2020-01-01"]
    """

    if format.lower() == 'date':
        return [datetime.datetime.now().strftime("%Y-%m-%d"), datetime.datetime.now().strftime("%Y-%m-%d")]
    elif format.lower() == 'datetime':
        return [datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), datetime.datetime.now().strftime("%Y-%m-%d %H:%M")]
    else:
        return [datetime.datetime.now().strftime("%Y-%m-%d"), datetime.datetime.now().strftime("%Y-%m-%d")]


def partition(values):
    """
    Partitions list into overlapping sublists of length 2.

    Args:
        values (list): List to be partitioned
    
    Returns:
        A list of sublists containing 2 elements each
    
    Examples:
        >>> values = ["Monday", 54, True]
        >>> partition(values) = [["Monday", 54], [54, True]]
    """

    if not isinstance(values, list):
        values = [values]

    new_list = []

    if len(values) == 1:
        new_list = [values + values]
    else:
        [new_list.append([values[i], values[i + 1]]) for i in range(len(values) - 1)]

    return new_list


def create_i18n_vocabulary(new_vocabulary: dict) -> I18nManager:
    """
    Create an I18nManager object which help in script internationalization

    Args:
        new_vocabulary: a dict containing the vocabulary in the desired languages.
    
    Returns:
        I18nManager object with vocabulary inserted as parameter
    
    Examples:
        >>> script_vocabulary = {"pt-br": {"frame_title": "Título do Frame", "table_title": "Tabela 01"},
                                 "en-us": {"frame_title": "Frame title", "table_title": "Table 01"}
                                }
        >>> script_terms = create_i18n_vocabulary(script_vocabulary)
        >>> table.title = script_terms.table_title
        >>> ResponseFrame([table], title=script_terms.frame_title)
     
        >>> # Tips And Tricks:
        >>> # One might be useful to define a pattern to name the labels, e.g.
        >>> vocabulary = {
        >>>     "pt-br": {
        >>>         "store_code_column_name": "Código Loja",
        >>>         "store_column_name": "Nome Loja",
        >>>         "goal_column_name": "Meta",
        >>>         "sale_column_name": "Venda",
        >>>     },
        >>>     "en-us": {
        >>>         "store_code_column_name": "Store code",
        >>>         "store_column_name": "Store name",
        >>>         "goal_column_name": "Goal",
        >>>         "sale_column_name": "Sale",
        >>>     }
        >>> }
    """
    i18n = I18nManager(language=GlobalCalling.looq.language)
    i18n.add_label(new_vocabulary)
    return i18n


def read_response_json(json_file: str, file_encoding='utf-8', **aditional_keys: str) -> dict:
    """
    Function used primarily in the Python-Template called by FES to reshape the response-json (sent by the Looqbox's
    Language Service) into a python readable format.
    """

    raw_file = open(json_file, 'r', encoding=file_encoding).read()
    formatted_file = _format_quotes(raw_file)
    json_content = _add_keys_to_json(json.loads(formatted_file), **aditional_keys)
    _update_global_variables(json_content)

    return json_content


def _format_quotes(text):
    formatter = QuoteFormatter(text)
    return formatter.format_quotes()


def _add_keys_to_json(json_content: dict, **aditional_keys) -> json:
    """
    Function used to add new keys to the response-json
    """

    _keys = {
        "featureFlags": aditional_keys.get("feature_flags", None),
        "domains": aditional_keys.get("domains", None),
    }

    for key, value in _keys.items():
        if value is not None:
            value = _format_quotes(value)
            json_content[key] = json.loads(value)

    return json_content


def _update_global_variables(json_content: dict) -> None:
    """
    Function used to update global variables
    """

    variables_to_add = {
        "feature_flags": json_content.get("featureFlags", None),
        "domains": json_content.get("domains", None),
        "question": json_content.get("question", {}).get("original", None),
    }

    for key, value in variables_to_add.items():
        if value is not None:
            GlobalCalling.looq.__setattr__(key, value)


def flatten(list_to_flat: list) -> list:
    flat_list = []
    for item in list_to_flat:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return [item for item in flat_list if item is not None]


def open_file(file, *path: str) -> TextIO:
    return open(os.path.join(file, *path))


def load_json_from_path(extraction_options_path):
    """Helper method to load a JSON file from a relative path"""
    with open(extraction_options_path, "r") as file:
        extract_options = json.load(file)
        file.close()
    return extract_options


def as_dict_ignore_nones(element):
    return asdict(element, dict_factory=lambda x: {k: v for (k, v) in x if v is not None})
