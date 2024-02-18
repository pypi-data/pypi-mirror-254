import json

from looqbox.config.logger import Logger
from looqbox.config.object_mapper import ObjectMapper
from looqbox.flows.steps.step import Step
from looqbox.objects.message.message import Message
from looqbox.objects.message.message_keys import MessageKeys
from looqbox.objects.response_parameters.response_parameters import ResponseParameters
from looqbox.objects.response_parameters.response_user import ResponseUser


# noinspection PyArgumentList
class LoadResponseParametersStep(Step):

    def __init__(self, message: Message):
        super().__init__(message)
        self.script_info = message.get(MessageKeys.SCRIPT_INFO)
        self.logger = Logger.get_logger(__name__)

    def execute(self):
        self.message.offer(
            (MessageKeys.RESPONSE_PARAMETERS, self._load_response_parameters())
        )

    def _load_response_parameters(self):
        with open(self.script_info.response_parameters_path, "r") as response_file:
            response_file_dict = json.load(response_file)
            try:
                self.response_parameters = ObjectMapper.map(response_file_dict, ResponseParameters)
            except Exception as e:
                self.logger.error(f"Error when mapping response parameters: {e}. \nUsing mocked version.")
                self.response_parameters = ResponseParameters(
                    question="mocked question",
                    user=ResponseUser(id=1, login="mocked login", group_id=1),
                    company_id=1
                )
            response_file.close()
        self.response_parameters.response_vars = self.script_info.response_vars
        return self.response_parameters
