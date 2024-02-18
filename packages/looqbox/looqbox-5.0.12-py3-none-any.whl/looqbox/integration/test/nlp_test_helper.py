import json
import os

from looqbox import ObjectMapper
from looqbox.flows.steps.set_natural_language_parameter_step import SetNaturalLanguageParameterStep
from looqbox.objects.message.message import Message
from looqbox.objects.message.message_keys import MessageKeys
from looqbox.objects.response_parameters.response_parameters import ResponseParameters
from looqbox.utils.utils import open_file


def open_file_in_directory(filename: str, path: str = "parser_reference"):
    return open_file(os.path.dirname(__file__), path, filename)


def set_nlp_values(filename: str, path: str = "parser_reference"):
    file = open_file_in_directory(filename, path)
    par = json.load(file)
    file.close()

    message = Message()
    par = ObjectMapper().map(par, ResponseParameters)
    message.offer((MessageKeys.RESPONSE_PARAMETERS, par))
    SetNaturalLanguageParameterStep(message).execute()

    return par
