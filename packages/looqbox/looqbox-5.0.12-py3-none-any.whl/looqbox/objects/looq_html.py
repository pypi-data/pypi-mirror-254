from looqbox.render.chatbot.components.text import _remove_html_tags
from looqbox.render.abstract_render import BaseRender
from looqbox.objects.looq_object import LooqObject
from looqbox.json_encoder import JsonEncoder
import json


class ObjHTML(LooqObject):
    """
    Wraps an HTML code in a Looqbox object to be used in the interface.
    """

    def __init__(self, html, tab_label=None, value=None):
        """
        Args:
            html (str): Html code that will be wrapped.
            tab_label (str): Set the name of the tab in the frame.

        Examples:
            >>> HTML = ObjHTML("<div> Hello Worlds </div>")
        """
        super().__init__()
        self.html = html
        self.tab_label = tab_label
        self.value = value

    def to_json_structure(self, visitor: BaseRender):
        return visitor.html_render(self)

    def __repr__(self):
        return _remove_html_tags(self.html) + self.value
