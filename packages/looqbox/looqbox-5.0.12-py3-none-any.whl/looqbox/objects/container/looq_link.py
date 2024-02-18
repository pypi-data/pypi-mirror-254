from looqbox.objects.container.abstract_container import AbstractContainer
from looqbox.render.abstract_render import BaseRender


class ObjLink(AbstractContainer):
    """
    Add a link to redirect the user to another question or external link.
    """

    def __init__(self, *children, question, **properties):
        """
        Args:
            children (list): Children to be contained.
            question (str): Question or external link to redirect the user.
            properties (dict): properties derived from parent like value, render_condition, tab_label, css_options. 
        
        Examples:
            >>> def add_link(value):
            >>>     return lq.ObjLink(lq.ObjText(value, css_options=[css.FontSize(16)]), question=value)
            >>>
            >>> df = pd.DataFrame({"col1": ["link1", "link2", "link3"]})
            >>> df["col1"] = df["col1"].apply(add_link)
        """
        super().__init__(*children, **properties)
        self.question = question
        self._auto_set_value()

    def __repr__(self):
        return f"{self.children}".replace("[", "").replace("]", "")

    def _auto_set_value(self):
        children_is_not_empty = self.children and len(self.children) == 1
        if children_is_not_empty:
            self.value = self.children[0].value

    def to_json_structure(self, visitor: BaseRender):
        return visitor.link_render(self)
