from looqbox.render.abstract_render import BaseRender
from looqbox.objects.looq_object import LooqObject


class ObjPDF(LooqObject):
    """
    Renders a PDF in the Looqbox's board using a PDF from the same directory of
    the response or from an external link (only works with HTTPS links).
    """
    def __init__(self, src, initial_page=1, default_scale=1.0, tab_label=None, value=None, **properties):
        """
        Args:
            src (str): PDF's source.
            initial_page (int, optional): Page that the PDF will open.
            default_scale (float, optional): Page's default scale
            tab_label (str, optional): Set the name of the tab in the frame.
            css_options (list, optional): set the correspond css property.

        Examples:
            >>> from looqbox import CssOption as Css
            >>> pdf = ObjPDF(src="cartaoCNPJLooqbox.pdf", 
            >>> default_scale=0.85, 
            >>> css_options=[Css.Height(200), Css.Width(400)])
        """
        super().__init__(**properties)
        self.source = src
        self.initial_page = initial_page
        self.tab_label = tab_label
        self.value = value
        self.default_scale = default_scale

    def to_json_structure(self, visitor: BaseRender):
        return visitor.pdf_render(self)
