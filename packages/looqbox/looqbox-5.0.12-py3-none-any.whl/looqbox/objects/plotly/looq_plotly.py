from looqbox.render.abstract_render import BaseRender
from looqbox.objects.looq_object import LooqObject


class ObjPlotly(LooqObject):
    """
    Creates an ObjPlotly from a plotly object.
    """
    def __init__(self, data, layout=None, stacked=True, display_mode_bar=True, tab_label=None, value=None, **kwargs):
        """
        Args:
            data (dict): Plotly general values. Can be a dict or a plotly object like Bar, Scatter and etc..
            layout (plotly.graph_objs._layout.Layout, optional): Layout elements of the plotly, it's a Layout object from
            plotly.graph_objs, if it's not send as a parameter, the function creates it internally.
            stacked (bool, optional): Define if the element should be stacked.
            display_mode_bar (bool, optional): Define if the mode bar in the top right of the graphic will appear or not.
            tab_label (str, optional): Set the name of the tab in the frame.

        Examples:
            >>> trace = go.Scatter(x = list(table.data['Data']), y = list(table.data['Venda']))
            >>> layout = go.Layout(title='title', yaxis=dict(title='Vendas'))
            >>> g = lq.ObjPlotly([trace], layout=layout)
        """
        super().__init__(**kwargs)
        self.data = data
        self.layout = layout
        self.stacked = stacked
        self.display_mode_bar = display_mode_bar
        self.tab_label = tab_label
        self.value = value

    def to_json_structure(self, visitor: BaseRender):
        return visitor.plotly_render(self)
