import datetime
import json
import logging
import sys
import warnings
from dataclasses import asdict
from typing import Callable

import pydantic_core
import requests
from multipledispatch import dispatch

from looqbox.class_loader.class_loader import ClassLoader
from looqbox.config.logger import Logger
from looqbox.config.object_mapper import ObjectMapper
from looqbox.database.database_functions import connect, sql_execute
from looqbox.database.connections.connection_big_query import BigQueryConnection
from looqbox.database.connections.connection_jdbc_query_executor import QueryExecutorJDBCConnection
from looqbox.database.connections.connection_mongo import MongoConnection
from looqbox.flows.steps.set_natural_language_parameter_step import SetNaturalLanguageParameterStep
from looqbox.global_calling import GlobalCalling
from looqbox.integration.language_response_integration.entity import get_entity
from looqbox.integration.language_response_integration.keyword import get_keyword
from looqbox.integration.language_response_integration.partition import get_partition
from looqbox.integration.looqbox_global import Looqbox
from looqbox.objects.api import ObjQuery
from looqbox.objects.message.message import Message
from looqbox.objects.message.message_keys import MessageKeys
from looqbox.objects.response_parameters.response_parameters import ResponseParameters
from looqbox.objects.response_parameters.response_question import ResponseQuestion
from looqbox.objects.response_parameters.response_user import ResponseUser
from looqbox.objects.visual.looq_message import ObjMessage
from looqbox.render.abstract_render import BaseRender
from looqbox.render.looqbox.base_looqbox_render import BrowserRender
from looqbox.utils.utils import load_json_from_path
from looqbox.view.response_board import ResponseBoard
from looqbox.view.response_frame import ResponseFrame
from looqbox.view.view_functions import frame_to_board
from looqbox.view.view_functions import response_to_frame

__all__ = ["look_tag", "looq_test_question", "view", "get_sso_attributes", "user_id", "user_group_id", "user_login",
           "question_link", "get_entity", "get_partition", "get_keyword", "_response_json_form"]

# Calling global variable
if GlobalCalling.looq.home is not None:
    GlobalCalling.set_looq_attributes(Looqbox())

logger = Logger.get_logger(__name__)


def _send_to_dev_link(url, response_board: ResponseBoard, show_json=False, visitor=None):
    """
    Function to test the return from scripts in Looqbox's interface

    :param url: Looqbox's client url
    :param response_board: Board resulting from the script
    :param show_json: Print JSON or not
    :return: A request from an api
    """

    if not visitor:
        visitor = BrowserRender()

    response_json = response_board.to_json_structure(visitor)

    if show_json is True:
        if isinstance(response_json, list) or isinstance(response_json, dict):
            print(json.dumps(response_json, indent=4))
        else:
            print(response_json)

    dev_link_header = build_request_header()

    try:
        link_request = requests.post(url, headers=dev_link_header, data=response_json)
    except requests.ConnectionError:
        logging.error("Page not found -> {0}".format(url))
        sys.exit(1)

    return link_request


def build_request_header() -> dict:
    header = {'x-rstudio-user': 'rstudio', 'Content-Type': 'application/json',
              "x-rstudio-pass": _get_rstudio_password()}

    return header


def _get_rstudio_password() -> str:
    from os import environ

    try:
        rstudio_pass = environ["RSTUDIO_PASS"]
    except:
        rstudio_pass = _get_rstudio_pass_locally()

    return rstudio_pass


def _get_rstudio_pass_locally() -> str:
    configuration_file = load_json_from_path(GlobalCalling.looq.config_file)
    try:
        return configuration_file["RSTUDIO_PASS"]
    except KeyError as error:
        raise Exception(f"Missing RSTUDIO_PASS in local configuration file")


def look_tag(tag, par_json, default=None, only_value=True, _deprecated=True):
    """
    Function to search for a specific tag inside the JSON sent by the parser

    :param tag: Name to be found
    :param par_json: JSON from parser
    :param default: Default value to be returned
    :param only_value: If True return only the value of the tag, if the value is False the function will return all
    the JSON structure link to this tag
    :param _deprecated: If True, will show a warning message
    :return: A JSON structure or a single value
    """

    if _deprecated:
        warnings.warn("look_tag is deprecated, use get_entity instead", DeprecationWarning, stacklevel=2)

    if tag == "$comparative":
        return have_comparative(par_json)

    try:
        message = Message()
        par = ObjectMapper().map(par_json, ResponseParameters)
        message.offer((MessageKeys.RESPONSE_PARAMETERS, par))
        SetNaturalLanguageParameterStep(message).execute()
    except pydantic_core.ValidationError:
        raise Exception("Invalid JSON")

    return get_entity(tag, par_json, entity_default=default, only_value=only_value)


def have_comparative(par_json):
    return "$comparative" in par_json["entities"].keys()


def _response_json(parser_json: ResponseParameters, function_call: Callable, second_call: bool = False) -> dict:
    """
    Function called by the python kernel inside the looqbox server. This function get the return in the main script
    and treat it to return a board to the frontend

    :param parser_json: JSON from parser
    :param function_call: Main function to be called inside the kernel. Default: looq_response
    :return: A ResponseBoard object (JSON)
    """

    response_parameters: ResponseParameters

    response_parameters = map_to_response_parameters(parser_json)

    GlobalCalling.looq.decimal_separator = response_parameters.user.dec_separator
    GlobalCalling.looq.date_format = response_parameters.user.date_format
    GlobalCalling.looq.language = response_parameters.user.language
    GlobalCalling.looq.user.login = response_parameters.user.login
    GlobalCalling.looq.user.id = response_parameters.user.id

    resp_par_json = asdict(response_parameters)

    try:
        response_parameters.question.original
    except AttributeError:
        question = response_parameters.question
        response_parameters.question = ResponseQuestion
        response_parameters.question.original = question
        response_parameters.question.clean = question

    if "$query" in response_parameters.question.original and not second_call:
        response = _response_query(response_parameters, function_call, second_call, simple=False)
    else:
        response = function_call(resp_par_json)
        is_board = isinstance(response, ResponseBoard)
        is_frame = isinstance(response, ResponseFrame)
        is_list = isinstance(response, list)

        if not is_frame and not is_board and is_list:
            response = frame_to_board(response)
        elif not is_frame and not is_board:
            looq_object = response_to_frame(response)
            response = frame_to_board(looq_object)
        elif is_frame:
            response = frame_to_board(response)

    visitor = _render_factory(response_parameters.device_type, response_parameters.app_type)
    board_json = response.to_json_structure(visitor)
    return board_json


def _render_factory(device_type: str, app_type: str = "") -> BaseRender:
    render_class = {
        "desktop": {
            "browser": "looqbox.render.looqbox.looqbox_desktop_render.DesktopBrowserRender",
            "whatsapp": "looqbox.render.chatbot.whatsapp_render.WhatsAppRender",
            "teams": "looqbox.render.chatbot.teams_render.TeamsRender",
            "chatbot": "looqbox.render.chatbot.base_chatbot_render.BaseChatbotRender"
        },
        "mobile": {
            "browser": "looqbox.render.looqbox.looqbox_mobile_render.MobileBrowserRender",
            "whatsapp": "looqbox.render.chatbot.whatsapp_render.WhatsAppRender",
            "teams": "looqbox.render.chatbot.teams_render.TeamsRender",
            "chatbot": "looqbox.render.chatbot.base_chatbot_render.BaseChatbotRender"
        }
    }

    # Default render is browser
    render_class = render_class.get(device_type.lower(), {}).get(
        app_type.lower(), "looqbox.render.looqbox.looqbox_desktop_render.DesktopBrowserRender"
    )
    class_path, class_name = render_class.rsplit(".", 1)
    return ClassLoader(class_name, class_path).call_class()


# noinspection PyBroadException
def _response_query(par: ResponseParameters, function_call: Callable, second_call: bool, simple: bool = False):
    response_execution_error = False
    # start_time = datetime.datetime.now()
    try:
        response = _response_json(par, function_call, second_call=True)
    except Exception as error:
        response_execution_error = True
    # total_sql_time = datetime.datetime.now() - start_time

    global_queries = GlobalCalling.looq.query_list.get(GlobalCalling.looq.session_id)
    queries_qt = len(global_queries)

    # If the global hasn't any query save
    if queries_qt == 0:
        message = ObjMessage("No query found in this response")
        response = ResponseFrame([message])
    else:
        response = ResponseFrame(stacked=True)
        # Reversing the list to change the appearing order in the looqbox frame
        global_queries.reverse()
        # For each query we save an objMessage inside a responseFrame
        total_time = _calculate_query_total_time(global_queries)
        response.content.insert(0, ObjQuery(queries=global_queries, total_time=str(total_time)))
        response = ResponseBoard([response])

    return response


def _calculate_query_total_time(global_queries):
    total_time = datetime.timedelta()
    batch_time = [datetime.timedelta()]
    # TODO refactor of total_time calculation
    for query in range(len(global_queries)):
        query_time = datetime.datetime.strptime(global_queries[query].get("time"), "%H:%M:%S.%f").time()
        query_time_delta = datetime.timedelta(
            hours=query_time.hour,
            minutes=query_time.minute,
            seconds=query_time.second,
            microseconds=query_time.microsecond
        )
        if global_queries[query]["mode"] == "single":
            total_time += query_time_delta
        else:
            batch_time.append(query_time_delta)
            if _add_batch_time(global_queries, query):
                total_time += max(batch_time)
                batch_time = [datetime.timedelta()]
    return total_time


def _add_batch_time(global_queries, query):
    return query == len(global_queries) - 1 or (
            query < len(global_queries) - 1 and global_queries[query + 1]["mode"] == "single")


def _check_test_parameter(parameters, par_name):
    """
    Function to check if the parameter_name(par_name) is on the parameter's keys

    :param parameters: Parameters send in looq_test_question
    :param par_name: Desire name to be found in key
    :return: The value of the par_name in parameter or None
    """
    par_return = None

    if hasattr(parameters, par_name):
        par_return = parameters[par_name]

    return par_return


def looq_test_question(test_function=None, parameters=None, show_json=False, user=None, host=None):
    """
    Function to simulate parser parameters. Using this developers can test their scripts using entities.

    :param test_function: Function to be tested, usually filled with looq_response
    :param parameters: Entities and its values
    :param show_json: Show final json or not
    :param user: User that the result will be sent
    :param host: Host that the result will be sent
    """
    # test when the process of response is correct
    if test_function is None:
        raise Exception("Function to be tested not been informed")

    if user is None:
        user = GlobalCalling.looq.user.login

    if host is None:
        host = GlobalCalling.looq.client_host

    if GlobalCalling.looq.test_mode is False:
        return None

    if isinstance(parameters, str):
        parameters = json.loads(parameters)

    response_parameters = map_to_response_parameters(parameters)

    visitor = _render_factory(response_parameters.device_type, response_parameters.app_type)

    if "$query" in parameters and parameters["$query"]:
        response = _response_query(parameters, test_function, second_call=False)
    else:
        initial_response_time = datetime.datetime.now()
        response = test_function(parameters)
        total_response_time = datetime.datetime.now() - initial_response_time

    if GlobalCalling.looq.publish_test is None or GlobalCalling.looq.publish_test is True:
        start_post_time = datetime.datetime.now()
        view(response, show_json, user, host, visitor)
        if "$query" in parameters and parameters["$query"]:
            print("Query Published")
        else:
            total_publish_time = datetime.datetime.now() - start_post_time
            print("Response time: " + str(total_response_time))
            print("Publish time: " + str(total_publish_time))
            print("Total time...:" + str(total_publish_time + total_response_time))


# noinspection PyArgumentList
def map_to_response_parameters(parameters):
    try:
        if isinstance(parameters, str):
            parameters = json.loads(parameters)
        if isinstance(parameters, ResponseParameters):
            return parameters
        parameters = ObjectMapper.map(parameters, ResponseParameters)
        message = Message()
        message.offer((MessageKeys.RESPONSE_PARAMETERS, parameters))
        SetNaturalLanguageParameterStep(message).execute()
        return parameters
    except:
        logger.info("Could not map parameters to ResponseParameters, please check your json")
        return ResponseParameters(
            question="mocked question",
            user=ResponseUser(id=1, login="mocked login", group_id=1),
            company_id=1
        )


def view(looq_object=None, show_json=False, user=GlobalCalling.looq.user.login,
         host=GlobalCalling.looq.client_host, visitor=None):
    if looq_object is None:
        actual_datetime = datetime.datetime.now()

        if looq_object is None:
            looq_object = ObjMessage(text="teste " + str(actual_datetime), type="alert-success")

    is_board = isinstance(looq_object, ResponseBoard)
    is_frame = isinstance(looq_object, ResponseFrame)
    is_list = isinstance(looq_object, list)

    if not is_frame and not is_board and is_list:
        looq_object = frame_to_board(looq_object)
    elif not is_frame and not is_board:
        looq_object = response_to_frame(looq_object)
        looq_object = frame_to_board(looq_object)
    elif is_frame:
        looq_object = frame_to_board(looq_object)
    url = host + "/api/devlink/" + user
    _send_to_dev_link(url, looq_object, show_json, visitor)
    print("looq.view: published for user", user, "in", host)


def _response_json_form(form_json, session_json, looq_process_form):
    """
    Function that will receive a form sent by the front. This function will read the parameters and execute then
    inside the looq_process_form in the other script.
    """

    response_parameters = map_to_response_parameters(form_json)

    GlobalCalling.looq.decimal_separator = response_parameters.user.dec_separator
    GlobalCalling.looq.date_format = response_parameters.user.date_format
    GlobalCalling.looq.language = response_parameters.user.language
    GlobalCalling.looq.user.login = response_parameters.user.login
    GlobalCalling.looq.user.id = response_parameters.user.id
    response = looq_process_form(form_json, session_json)

    is_board = isinstance(response, ResponseBoard)
    is_frame = isinstance(response, ResponseFrame)
    is_list = isinstance(response, list)

    if not is_frame and not is_board and is_list:
        response = frame_to_board(response)
    elif not is_frame and not is_board:
        looq_object = response_to_frame(response)
        response = frame_to_board(looq_object)
    elif is_frame:
        response = frame_to_board(response)

    visitor = _render_factory(response_parameters.device_type, response_parameters.app_type)

    board_json = response.to_json_structure(visitor)

    return board_json


def get_sso_attributes(par):
    """
    Get the user SSO information from parser

    :return: The JSON of userSsoAttributes in parser return
    """
    sso_attributes = None

    if par is None:
        par = {"apiVersion": 1}

    if "apiVersion" not in par.keys() or par["apiVersion"] is None:
        sso_attributes = par["userSsoAttributes"]

    elif par["apiVersion"] == 1:
        sso_attributes = par["userSsoAttributes"]

    elif par["apiVersion"] >= 2:
        sso_attributes = par["user"]["ssoAttributes"]

    return sso_attributes


def question_link(question, link_text):
    """
    Creates a link to a question.

    :param str question: Question.
    :param str link_text: Text of the link.
    :return: A link string.
    """
    return "<question-link query='" + question + "'>" + link_text + "</question-link>"


def user_id(par: dict = None) -> str:
    """
    Get the user id from options(par is None) or from parser.

    Examples:
    --------
    >>> user_id(par)

    :return: The id string.
    """
    if par is None:
        return GlobalCalling.looq.user.id
    else:
        return par.get('user').get('id')


def user_login(par: dict = None) -> str:
    """
    Get the user login from options(par is None) or from parser.

    Examples:
    --------
    >>> user_login(par)

    :return: The login string.
    """
    if par is None:
        return GlobalCalling.looq.user.login
    else:
        return par.get('user').get('login')


def user_group_id(par: dict = None) -> str:
    """
    Get the user group id from options(par is None) or from parser.

    Examples:
    --------
    >>> user_group_id(par)

    :return: The group id string.
    """
    if par is None:
        return GlobalCalling.looq.user.group
    else:
        return par.get('user').get('groupId')


def _test_connection(connection_name: str) -> str:
    try:
        connection = connect(connection_name)
        execute_test_query(connection)
        is_connection_functional = True
    except Exception as connection_error:
        is_connection_functional = False
        raise connection_error

    return str(is_connection_functional).upper()


@dispatch(QueryExecutorJDBCConnection)
def execute_test_query(connection: QueryExecutorJDBCConnection) -> None:
    test_query = "Select 1"
    sql_execute(connection, test_query)


@dispatch(BigQueryConnection)
def execute_test_query(connection: BigQueryConnection) -> None:
    test_query = "Select 1"
    sql_execute(connection, test_query)


@dispatch(MongoConnection)
def execute_test_query(connection: MongoConnection) -> None:
    test_query = {"collection": "test",
                  "query": {},
                  "fields": {"_id": 1},
                  "limit": 1
                  }
    sql_execute(connection, test_query)
