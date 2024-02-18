from looqbox.flows.steps.step import Step
from looqbox.objects.message.message import Message
from looqbox.objects.message.message_keys import MessageKeys


class ResponseWriterStep(Step):
    def __init__(self, message: Message):
        super().__init__(message)
        self.script_info = message.get(MessageKeys.SCRIPT_INFO)
        self.response = message.get(MessageKeys.RESPONSE)
    def execute(self):
        with open(self.script_info.result_path, 'w') as file:
            file.write(self.response)
            file.close()

