from looqbox.render.abstract_render import BaseRender
from looqbox.objects.looq_object import LooqObject


class ObjAudio(LooqObject):
    """
    Creates a Looqbox audio object from an audio file which is in the same directory of the script or from a https
    web link.
    """

    def __init__(self, src, auto_play=False, tab_label=None, value=None):
        """     
        Args:
            src (str): Source of the audio to be displayed (filepath or https link).
            auto_play (bool): Defines if the audio starts as soon as the board is opened.

        Examples:
            >>> audio = ObjAudio("/Users/looqbox/Downloads/armstrong.mp3")
        """
        super().__init__()
        self.source = src
        self.auto_play = auto_play
        self.tab_label = tab_label
        self.value = value

    def to_json_structure(self, visitor: BaseRender):
        return visitor.video_render(self)

