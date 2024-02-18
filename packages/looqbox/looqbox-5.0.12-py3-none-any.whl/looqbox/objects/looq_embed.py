from looqbox.render.abstract_render import BaseRender
from looqbox.objects.looq_object import LooqObject


class ObjEmbed(LooqObject):
    """
    Creates a frame inside the Looqbox interface using an iframe HTML tag as source.
    """
    def __init__(self, iframe, tab_label=None, value=None):
        """
        Args:
            iframe (str): Embedded element dimensions and source in HTML format.

        Examples:
            >>> webframe0 = ObjEmbed("<iframe frameborder=\"0\" width=\"560\" height=\"315\"
            >>>                 src=\"https://app.biteable.com/watch/embed/looqbox-presentation-1114895\">
            >>>                 </iframe>")
        """
        super().__init__()
        self.iframe = iframe
        self.tab_label = tab_label
        self.value = value

    def to_json_structure(self, visitor: BaseRender):
        return visitor.embed_render(self)
