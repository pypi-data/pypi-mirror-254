from looqbox.render.abstract_render import BaseRender
from looqbox.objects.looq_object import LooqObject


class ResponseFrame(LooqObject):
    """
    Class that represents the response frame object.
    """

    def __init__(self, content=None, frame_class=None, style=None, stacked=True, title=None, tab_view=False,
                 insights=None):
        """
        Args:
            content (list): List of content objects
            frame_class (list): List of classes
            style (dict): Dictionary of styles
            stacked (bool): If the frame is stacked
            title (str): Title of the frame
            tab_view (bool): If the frame is a tab view
            insights (dict): Dictionary of insights
        
        Examples:
            >>> frame = lq.ResponseFrame([lq.ObjMessage("Hello World")])
        """
        super().__init__()
        if frame_class is None:
            frame_class = []
        if content is None:
            content = []
        if title is None:
            title = []
        if style is None:
            style = {}
        if insights is None:
            insights = {}
        # Convert a simple string in to list
        if isinstance(title, str):
            title = [title]

        self.content = content
        self.frame_class = frame_class
        self.style = style
        self.stacked = stacked
        self.title = title
        self.tab_view = tab_view
        self.insights = insights

    def to_json_structure(self, visitor: BaseRender):
        return visitor.response_frame_render(self)

    # @property
    # def to_json_structure(self):
    #     # Dynamic error message to help the users to understand the error
    #     if type(self.content) is not list:
    #         raise TypeError("Content is not a list")
    #
    #     objects_json_list = [json.loads(looq_object.to_json_structure) for looq_object in
    #                          self.content if looq_object is not None]
    #
    #     json_content = OrderedDict(
    #         {
    #             'type': 'frame',
    #             'class': self.frame_class,
    #             'content': objects_json_list,
    #             'style': self.style,
    #             'stacked': self.stacked,
    #             'title': self.title,
    #             'tabView': self.tab_view,
    #             'insights': self.insights
    #         }
    #     )
    #
    #     # Transforming in JSON
    #     frame_json = json.dumps(json_content, indent=1, allow_nan=True, cls=JsonEncoder)
    #
    #     return frame_json
