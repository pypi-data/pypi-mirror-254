from dataclasses import asdict

from looqbox.flows.steps.step import Step
from looqbox.global_calling import GlobalCalling
from looqbox.objects.message.message import Message
from looqbox.objects.message.message_keys import MessageKeys

global_variables = GlobalCalling().looq


class DefineGlobalVariablesStep(Step):

    def __init__(self, message: Message):
        super().__init__(message)
        self.script_info = message.get(MessageKeys.SCRIPT_INFO)
        self.response_parameters = message.get(MessageKeys.RESPONSE_PARAMETERS)

    def execute(self):
        for key, value in asdict(self.script_info.response_vars).items():
            setattr(global_variables, key, value)
        global_variables.question = str(self.response_parameters.question)

