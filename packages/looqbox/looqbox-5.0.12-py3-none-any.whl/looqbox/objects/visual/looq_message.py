from looqbox.render.abstract_render import BaseRender
from looqbox.objects.looq_object import LooqObject


class ObjMessage(LooqObject):
    """
    Creates a looqbox standard message box.
    """

    def __init__(self, text, type="alert-default", align="center", style=None, tab_label=None, value=None):
        """
        Args:
            text (str): Text to be displayed.
            type (str, optional): Type of the message. Types: alert-warning (yellow), alert-danger (red), 
                alert-success (green), alert-default (gray), alert-info (blue). Defaults to "alert-default".
            align (str, optional): Text align. Defaults to "center".
            style (dict, optional): A dict of CSS styles to change the frame. Defaults to None.
            tab_label (str, optional): Set the name of the tab in the frame. Defaults to None.
            value (str, optional): Defaults to None.

        Examples:
            >>> message = ObjMessage("Teste!", type='alert-warning')
        """
        super().__init__()
        if style is None:
            style = {}
        self.text = text
        self.text_type = type
        self.text_align = align
        self.text_style = style
        self.tab_label = tab_label
        self.value = value

    def to_json_structure(self, visitor: BaseRender):
        return visitor.message_render(self)
