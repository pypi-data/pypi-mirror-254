from looqbox.flows.steps.step import Step
from looqbox.global_calling import GlobalCalling
from looqbox.objects.message.message import Message
from looqbox.objects.message.message_keys import MessageKeys
from looqbox.utils.dot_notation import Functional

global_variables = GlobalCalling().looq


class SetNaturalLanguageParameterStep(Step):

    def __init__(self, message: Message):
        super().__init__(message)
        self.response_parameters = message.get(MessageKeys.RESPONSE_PARAMETERS)

    def execute(self):
        global_variables.response_parameters = self.response_parameters
        global_variables.response_filters = Functional(self.response_parameters.conditions).associate_by_not_none(lambda it: it.get_entity_type())
        global_variables.response_partitions = self.response_parameters.group_by
        global_variables.response_keywords = self.response_parameters.keywords
        global_variables.syntax_tree = self.response_parameters.syntax_tree
