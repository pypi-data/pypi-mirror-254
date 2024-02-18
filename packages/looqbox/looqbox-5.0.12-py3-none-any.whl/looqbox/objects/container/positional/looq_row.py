from looqbox.objects.container.positional.abstract_positional_container import AbstractPositionalContainer
from looqbox.render.abstract_render import BaseRender


class ObjRow(AbstractPositionalContainer):
    """
    Class to create a row container. Children will be displayed horizontally.
    """

    def __init__(self, *children, **properties):
        """
        Args:
            *children (Any): Children to be contained.
            **properties (dict): Properties derived from parent like value, render_condition, tab_label, css_options.

        Examples:
            >>> ObjRow(
            >>>     lq.ObjPlotly(monthly_chart, display_mode_bar=False, tab_label="Mensal"),
            >>>     lq.ObjPlotly(annual_chart, display_mode_bar=False, tab_label="Anual")
            >>> )
        """
        super().__init__(*children, **properties)

    def to_json_structure(self, visitor: BaseRender):
        return visitor.row_render(self)
