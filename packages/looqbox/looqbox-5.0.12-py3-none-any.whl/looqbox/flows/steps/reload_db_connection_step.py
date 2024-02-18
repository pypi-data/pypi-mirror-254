from looqbox.database.database_functions import reload_database_connection
from looqbox.flows.steps.step import Step
from looqbox.objects.message.message import Message
from looqbox.objects.message.message_keys import MessageKeys


class ReloadDbConnectionStep(Step):

    def __init__(self, message: Message):
        super().__init__(message)
        self.script_info = message.get(MessageKeys.SCRIPT_INFO)
        self.response_parameters = message.get(MessageKeys.RESPONSE_PARAMETERS)

    def execute(self):
        reload_database_connection()
