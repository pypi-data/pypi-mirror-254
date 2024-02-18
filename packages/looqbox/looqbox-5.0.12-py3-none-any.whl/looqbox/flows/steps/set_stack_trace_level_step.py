import os

from looqbox.flows.steps.step import Step
from looqbox.global_calling import GlobalCalling
from looqbox.utils.utils import load_json_from_path

global_variables = GlobalCalling.looq


class SetStackTraceLevelStep(Step):
    def execute(self):
        import sys
        flow_settings_path = os.path.join(
            os.path.dirname(__file__),
            "..", "..",
            "resources", "flow_setting.json")

        if global_variables.test_mode:
            flow_setting = load_json_from_path(flow_settings_path)
            sys.tracebacklimit = flow_setting.get("stackTraceLevel", 0)
        else:
            sys.tracebacklimit = None
