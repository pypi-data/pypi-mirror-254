import numpy as np

from looqbox.objects.visual.abstract_visual_component import AbstractVisualComponent
from looqbox.render.abstract_render import BaseRender


class ObjGauge(AbstractVisualComponent):
    """
    Creates a gauge visual component with configurable traces.
    """

    def __init__(self, *traces, animated=True, **properties):
        """
        Args:
            traces (list): Traces are a set of dictionaries containing all gauge info.
                Each trace dictionary can contain:
                    - value (float): The value to be displayed.
                    - label (str): The label to be displayed within a tooltip on trace hover.
                    - scale_min (float, optional): Minimum value used on gauge scale. Defaults to 0.
                    - scale_max (float, optional): Maximum value used on gauge scale. Defaults to 1.
                    - value_format (str, optional): Format option to be applied on the values. Defaults to "percent:0".
                    - color (str | dict | function): Determines the color of each trace. 
                        It can be a string (e.g., "#48F86E"), a dictionary specifying gradients, or a function returning either.
            animated (bool, optional): Boolean to indicate if it should be animated. Defaults to True.
            properties (dict, optional): Inherited properties.

        Examples:
            >>> trace_0 = {
            >>>     "value": 0.4,
            >>>     "label": "Store A: 40%",
            >>> }
            >>> trace_1 = {
            >>>     "value": 0.2,
            >>>     "label": "Store B: 20%",
            >>>     "color": "#48F86E"
            >>> }
            >>> gauge = ObjGauge(trace_0, trace_1)
        """
        super().__init__(**properties)
        self.traces = list(np.hstack(traces)) if traces else []
        self.animated = animated

    def add_default_color_schema(self) -> None:

        default_colors = self.get_default_colors()
        for trace in range(len(self.traces)):
            if "color" not in self.traces[trace]:
                self.traces[trace]["color"] = default_colors

    def _get_default_style(self) -> None:
        import os
        import json

        default_style_file = open(os.path.join(os.path.dirname(__file__), "..", "..",
                                               "resources", "default_style.json"))

        default_colors = json.load(default_style_file)
        default_style_file.close()
        self._default_style = default_colors.get(self.__class__.__name__)

    def get_default_colors(self) -> dict:
        return self._default_style.get("colorSchema")

    def to_json_structure(self, visitor: BaseRender):
        self._get_default_style()
        self.add_default_color_schema()
        return visitor.gauge_render(self)
