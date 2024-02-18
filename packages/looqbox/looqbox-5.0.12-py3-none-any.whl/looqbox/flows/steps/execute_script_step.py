import importlib.util

from looqbox.flows.steps.step import Step
from looqbox.global_calling import GlobalCalling
from looqbox.integration.integration_links import _response_json
from looqbox.objects.message.message import Message
from looqbox.objects.message.message_keys import MessageKeys


class ExecuteScriptStep(Step):
    def __init__(self, message: Message):
        super().__init__(message)
        self.script_info = message.get(MessageKeys.SCRIPT_INFO)
        self.response_parameters = message.get(MessageKeys.RESPONSE_PARAMETERS)

    def execute(self):
        response = self._load_and_exec_module()
        self.message.offer((
            MessageKeys.RESPONSE, response
        ))

    def _load_and_exec_module(self):
        spec = importlib.util.spec_from_file_location(
            "executed_script",
            self.script_info.response_vars.response_path
        )
        script_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(script_module)  # This publishes to the interface
        try:
            response = _response_json(self.response_parameters, script_module.looq_response)
            return response
        except Exception as error:
            self._remove_query_from_global_list()
            raise Exception from error

    @staticmethod
    def _remove_query_from_global_list() -> None:
        try:
            del GlobalCalling.looq.query_list[GlobalCalling.looq.session_id]
        except KeyError as error:
            print(KeyError(f"Could not find session id in queries list: {error}"))
