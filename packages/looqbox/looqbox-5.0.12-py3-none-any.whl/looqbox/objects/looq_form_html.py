from looqbox.render.abstract_render import BaseRender
from looqbox.objects.looq_object import LooqObject


class ObjFormHTML(LooqObject):
    """
    Creates a Looqbox form HTML object.
    """

    def __init__(self, filepath=None, html=None, content=[], tab_label=None, value=None):
        """
        Args:
            html (str): HTML string to be executed.
            filepath (str, optional): Form input file path. Defaults to None.
            content (str, optional): Form content. Defaults to None.
            tab_label (str, optional): Set the name of the tab in the frame. Defaults to None.

        Examples:
        """
        super().__init__()
        self.html = html
        self.filepath = filepath
        self.content = content
        self.tab_label = tab_label
        self.value = value

    def to_json_structure(self, visitor: BaseRender):
        return visitor.form_html_render(self)
