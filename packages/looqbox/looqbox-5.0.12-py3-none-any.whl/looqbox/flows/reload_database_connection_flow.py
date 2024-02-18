from __future__ import annotations

from looqbox.flows.base_flow import BaseFlow
from looqbox.flows.steps.define_global_variables_step import DefineGlobalVariablesStep
from looqbox.flows.steps.load_response_parameters_step import LoadResponseParametersStep
from looqbox.flows.steps.reload_db_connection_step import ReloadDbConnectionStep
from looqbox.flows.steps.response_writer_step import ResponseWriterStep


class ReloadDatabaseConnectionFlow(BaseFlow):

    def define_steps(self):
        self.steps = [
            LoadResponseParametersStep,
            DefineGlobalVariablesStep,
            ReloadDbConnectionStep,
            ResponseWriterStep
        ]
