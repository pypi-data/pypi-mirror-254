from looqbox.flows.base_flow import BaseFlow
from looqbox.flows.steps.define_global_variables_step import DefineGlobalVariablesStep
from looqbox.flows.steps.load_response_parameters_step import LoadResponseParametersStep
from looqbox.flows.steps.test_connection_step import TestConnectionStep


class TestConnectionFlow(BaseFlow):

    def define_steps(self):
        self.steps = [
            LoadResponseParametersStep,
            DefineGlobalVariablesStep,
            TestConnectionStep
        ]
