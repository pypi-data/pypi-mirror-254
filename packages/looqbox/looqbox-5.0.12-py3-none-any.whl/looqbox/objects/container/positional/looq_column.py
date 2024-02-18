from looqbox.objects.container.positional.abstract_positional_container import AbstractPositionalContainer
from looqbox.render.abstract_render import BaseRender


class ObjColumn(AbstractPositionalContainer):
    """
    Class to create a column container. Children will be displayed vertically.
    """

    def __init__(self, *children, **properties):
        """
        Args:
            *children (Any): Children to be contained.
            **properties (dict): Properties derived from parent like value, render_condition, tab_label, css_options.
        
        Examples:
            >>> ObjColumn(
            >>>     lq.ObjPlotly(chart_1),
            >>>     lq.ObjPlotly(chart_2)
            >>> )
        """
        super().__init__(*children, **properties)

    def to_json_structure(self, visitor: BaseRender):
        return visitor.column_render(self)
