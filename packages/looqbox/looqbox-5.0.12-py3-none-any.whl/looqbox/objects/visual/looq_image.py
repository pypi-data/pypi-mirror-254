from looqbox.render.abstract_render import BaseRender
from looqbox.objects.looq_object import LooqObject


class ObjImage(LooqObject):
    """
    Creates a looqbox image object.
    """

    def __init__(self, src, width=None, height=None, style=None, tooltip=None, link=None, tab_label=None, value=None):
        """
        Args:
            src (str): Image source.
            width (int, optional): Image width. Defaults to None.
            height (int, optional): Image height. Defaults to None.
            style (dict, optional): A dict of CSS styles to change the frame. Defaults to None.
            tooltip (str, optional): Text in pop-up message. Defaults to None.
            link (str, optional): Add link to image. Defaults to None.
            tab_label (str, optional): Set the name of the tab in the frame. Defaults to None.

        Examples:
            >>> img = ObjImage(
            >>>     src="http://www.velior.ru/wp-content/uploads/2009/05/Test-Computer-Key-by-Stuart-Miles.jpg",
            >>>     width=100,
            >>>     height=100,
            >>>     style={"border-radius": "8px"},
            >>>     tooltip="test",
            >>>     link="https://www.looqbox.com/"
            >>> )
        """
        super().__init__()
        if link is None:
            link = {}
        if tooltip is None:
            tooltip = {}
        if style is None:
            style = []
        self.source = src
        self.width = width
        self.height = height
        self.style = style
        self.tooltip = tooltip
        self.link = link
        self.tab_label = tab_label
        self.value = value

    def to_json_structure(self, visitor: BaseRender):
        return visitor.image_render(self)

    def __repr__(self):
        return f"{self.value}"
