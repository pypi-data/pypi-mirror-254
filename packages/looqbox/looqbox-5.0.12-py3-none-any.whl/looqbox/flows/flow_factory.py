from __future__ import annotations

import json

from looqbox.config.object_mapper import ObjectMapper
from looqbox.flows.reload_database_connection_flow import ReloadDatabaseConnectionFlow
from looqbox.flows.script_flow import ScriptFlow
from looqbox.flows.script_response_form_flow import ScriptResponseFormFlow
from looqbox.flows.test_connection_flow import TestConnectionFlow
from looqbox.objects.flow.flow_type import FlowType
from looqbox.objects.flow.script_info import ScriptInfo


class FlowFactory:

    def __init__(self, script_info: str):
        script_info_dict = json.loads(script_info)
        self.script_info = ObjectMapper.map(script_info_dict, ScriptInfo)
        self.flow_types = {
            FlowType.LOOQ_TEST_CONN: TestConnectionFlow,
            FlowType.LOOQ_RESPONSE: ScriptFlow,
            FlowType.LOOQ_RELOAD_DATABASE_CONNECTIONS: ReloadDatabaseConnectionFlow,
            FlowType.LOOQ_RESPONSE_FORM: ScriptResponseFormFlow
        }

    @property
    def get_flow(self):
        return self.flow_types[self.script_info.flow_type](self.script_info)
