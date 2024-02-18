from looqbox.objects.container.abstract_container import AbstractContainer
from looqbox.render.abstract_render import BaseRender


class ObjTooltip(AbstractContainer):
    """
    Class to add a tooltip to a component.
    """

    def __init__(self, *children, text, **properties):
        """
        Args:
            children (Any): Children to be contained.
            text (str): Text to be displayed on mouse hover.
            properties (dict): properties derived from parent like value, render_condition, tab_label, css_options.

        Methods:
            set_orientation_top: Set the orientation of the tooltip to top.
            set_orientation_right: Set the orientation of the tooltip to right.
            set_orientation_bottom: Set the orientation of the tooltip to bottom.
            set_orientation_left: Set the orientation of the tooltip to left.
            set_orientation_top_left: Set the orientation of the tooltip to top left.
            set_orientation_top_right: Set the orientation of the tooltip to top right.
            set_orientation_bottom_left: Set the orientation of the tooltip to bottom left.
            set_orientation_bottom_right: Set the orientation of the tooltip to bottom right.
            set_orientation_left_top: Set the orientation of the tooltip to left top.
            set_orientation_left_bottom: Set the orientation of the tooltip to left bottom.
            set_orientation_right_top: Set the orientation of the tooltip to right top.
            set_orientation_right_bottom: Set the orientation of the tooltip to right bottom.
        
        Examples:
            >>> ObjTooltip(
            >>>     text="Hover me"
            >>> )
        """
        super().__init__(*children, **properties)
        self.text = text
        self.orientation = "top"

    def to_json_structure(self, visitor: BaseRender):
        return visitor.tooltip_render(self)

    @property
    def set_orientation_top(self):
        self.orientation = "top"
        return self

    @property
    def set_orientation_right(self):
        self.orientation = "right"
        return self

    @property
    def set_orientation_bottom(self):
        self.orientation = "bottom"
        return self

    @property
    def set_orientation_left(self):
        self.orientation = "left"
        return self

    @property
    def set_orientation_top_left(self):
        self.orientation = "topLeft"
        return self

    @property
    def set_orientation_top_right(self):
        self.orientation = "topRight"
        return self

    @property
    def set_orientation_bottom_left(self):
        self.orientation = "bottomLeft"
        return self

    @property
    def set_orientation_bottom_right(self):
        self.orientation = "bottomRight"
        return self

    @property
    def set_orientation_left_top(self):
        self.orientation = "leftTop"
        return self

    @property
    def set_orientation_left_bottom(self):
        self.orientation = "leftBottom"
        return self

    @property
    def set_orientation_right_top(self):
        self.orientation = "rightTop"
        return self

    @property
    def set_orientation_right_bottom(self):
        self.orientation = "rightBottom"
        return self
