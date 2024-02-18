from looqbox.flows.steps.step import Step
from looqbox.global_calling import GlobalCalling


class RemoveQueryFromGlobalListStep(Step):
    def execute(self):
        try:
            del GlobalCalling.looq.query_list[GlobalCalling.looq.session_id]
        except KeyError as error:
            print(KeyError(f"Could not find session id in queries list: {error}"))
