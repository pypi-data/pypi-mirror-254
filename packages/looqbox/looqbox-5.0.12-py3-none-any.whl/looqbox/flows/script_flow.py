from looqbox.flows.base_flow import BaseFlow
from looqbox.flows.steps.define_global_variables_step import DefineGlobalVariablesStep
from looqbox.flows.steps.execute_script_step import ExecuteScriptStep
from looqbox.flows.steps.load_response_parameters_step import LoadResponseParametersStep
from looqbox.flows.steps.remove_query_from_global_list_step import RemoveQueryFromGlobalListStep
from looqbox.flows.steps.response_writer_step import ResponseWriterStep
from looqbox.flows.steps.set_natural_language_parameter_step import SetNaturalLanguageParameterStep
from looqbox.flows.steps.set_stack_trace_level_step import SetStackTraceLevelStep


class ScriptFlow(BaseFlow):
    script_module = None

    def define_steps(self) -> None:
        self.steps = [
            LoadResponseParametersStep,
            DefineGlobalVariablesStep,
            SetNaturalLanguageParameterStep,
            SetStackTraceLevelStep,
            ExecuteScriptStep,
            RemoveQueryFromGlobalListStep,
            ResponseWriterStep
        ]
