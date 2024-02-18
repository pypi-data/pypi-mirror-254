from looqbox.integration.looqbox_global import Looqbox
from looqbox.objects.flow.script_info import ScriptInfo
from looqbox.objects.message.key import Key
from looqbox.objects.response_parameters.response_parameters import ResponseParameters


@Key.delegate
class MessageKeys:
    SCRIPT_INFO: ScriptInfo
    RESPONSE_PARAMETERS: ResponseParameters
    RESPONSE: str
