from looqbox.render.abstract_render import BaseRender
from looqbox.objects.looq_object import LooqObject


class ObjForm(LooqObject):
    """
    Creates a Looqbox form.
    """

    def __init__(self, *fields, title=None, method="GET", action=None, filepath=None, tab_label=None, value=None):
        """
        Args:
            fields (dict): Form parameters.
            title (str, optional): Form title. Defaults to None.
            method (str, optional): Form method ("GET" or "POST"). Defaults to "GET".
            action (str, optional): Form action. Defaults to None.
            filepath (str, optional): Form input file path. Defaults to None.
            tab_label (str, optional): Set the name of the tab in the frame. Defaults to None.

        Example:
            >>> form = ObjForm({"type": "input", "label": "Loja", "value": "3",
            >>>     "name": "loja", "readonly": TRUE, "style": {"text-align": "center"}},
            >>>     {"type": "input", "label": "Produto", "value": "Suco",
            >>>     "name": "plu", "readonly": TRUE, "style": {"text-align": "center"}},
            >>>     title="Suco de laranja 350mL")
        """
        super().__init__()
        if action is None:
            action = ""
        self.title = title
        self.method = method
        self.action = action
        self.filepath = filepath
        self.fields = fields
        self.tab_label = tab_label
        self.value = value

    def to_json_structure(self, visitor: BaseRender):
        return visitor.obj_form_render(self)
