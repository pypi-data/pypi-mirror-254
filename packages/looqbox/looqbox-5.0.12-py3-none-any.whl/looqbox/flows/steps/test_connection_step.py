from looqbox.flows.steps.step import Step
from looqbox.integration.integration_links import _test_connection
from looqbox.objects.message.message import Message
from looqbox.objects.message.message_keys import MessageKeys


class TestConnectionStep(Step):

    def __init__(self, message: Message):
        super().__init__(message)
        self.script_info = message.get(MessageKeys.SCRIPT_INFO)
        self.response_parameters = message.get(MessageKeys.RESPONSE_PARAMETERS)

    def execute(self):
        conn_name = self.response_parameters.connection_name
        is_connection_working = _test_connection(conn_name)
        with open(self.script_info.result_path, "w") as result_file:
            result_file.write(is_connection_working)
            result_file.close()
