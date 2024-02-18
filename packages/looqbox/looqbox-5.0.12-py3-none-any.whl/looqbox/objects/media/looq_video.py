from looqbox.render.abstract_render import BaseRender
from looqbox.objects.looq_object import LooqObject


class ObjVideo(LooqObject):
    """
    Creates a looqbox video object from a video file in the same directory of the script or from a https web link.
    """
    def __init__(self, src, auto_play=False, tab_label=None, value=None):
        """
        Args:
            src (str): Source of the video to be displayed.
            auto_play (bool, optional): Defines if the video starts as soon as the board is opened. Defaults to False.
            tab_label (str, optional): Set the name of the tab in the frame. Defaults to None.

        Examples:
            >>> video = ObjVideo("videoFile")
        """
        super().__init__()
        self.source = src
        self.auto_play = auto_play
        self.tab_label = tab_label
        self.value = value

    def to_json_structure(self, visitor: BaseRender):
        return visitor.video_render(self)
