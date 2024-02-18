from looqbox.objects.container.abstract_container import AbstractContainer
from looqbox.render.abstract_render import BaseRender
from looqbox.objects.component_utility.css_option import CssOption as css


class ObjSwitch(AbstractContainer):
    """
    Create a switch to change the object that will be displayed.
    """

    def __init__(self, *children, should_remove_top_space=True, **properties):
        """
        Args:
            *children (Any): Children to be contained.
            should_remove_top_space (bool): Remove the top space of the switch.
            **properties (dict): Properties derived from parent like value, render_condition, tab_label, css_options.
        
        Methods:
            set_orientation_right: Set the orientation of the switch to right.
            set_orientation_center: Set the orientation of the switch to center.
            set_orientation_left: Set the orientation of the switch to left.
        
        Examples:
            >>> ObjSwitch(
            >>>     lq.ObjPlotly(monthly_chart, display_mode_bar=False, tab_label="Mensal"),
            >>>     lq.ObjPlotly(annual_chart, display_mode_bar=False, tab_label="Anual")
            >>> )   
        """
        super().__init__(*children, **properties)
        self.orientation = "right"
        if should_remove_top_space:
            self._remove_empty_space()

    def to_json_structure(self, visitor: BaseRender):
        return visitor.switch_render(self)

    @property
    def set_orientation_right(self):
        self.orientation = "right"
        return self

    @property
    def set_orientation_center(self):
        self.orientation = "center"
        return self

    @property
    def set_orientation_left(self):
        self.orientation = "left"
        return self

    def _remove_empty_space(self):
        self.css_options = css.add(self.css_options, css.Position("absolute"))
        self.css_options = css.add(self.css_options, css.ZIndex(2))
