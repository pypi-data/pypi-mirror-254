from looqbox.render.abstract_render import BaseRender
from looqbox.objects.looq_object import LooqObject


class ObjWebFrame(LooqObject):
    """
    Creates a looqbox web frame from a web content link. 
    Note: Only works with HTTPS links due to web security reasons.
    """
    
    def __init__(self, src, width=None, height=500, enable_fullscreen=False,
                 open_fullscreen=False, tab_label=None, value=None):
        """
        Args:
            src (str): HTTPS web link of the content.
            width (int, optional): Width of the frame to be displayed in the interface. Defaults to None.
            height (int, optional): Height of the frame to be displayed in the interface. Defaults to 500.
            enable_fullscreen (bool, optional): Enable "fullscreen" button. Defaults to False.
            open_fullscreen (bool, optional): If True, the web frame is opened in fullscreen mode inside the interface. Defaults to False.
            tab_label (str, optional): Set the name of the tab in the frame. Defaults to None.
            value (optional): Defaults to None.

        Examples:
            >>> frame = ObjWebFrame("https://toggl.com/online-stopwatch/", width=500, height=480)
        """
        super().__init__()
        self.source = src
        self.width = width
        self.height = height
        self.enable_fullscreen = enable_fullscreen
        self.open_fullscreen = open_fullscreen
        self.tab_label = tab_label
        self.value = value

    def to_json_structure(self, visitor: BaseRender):
        return visitor.web_frame(self)
