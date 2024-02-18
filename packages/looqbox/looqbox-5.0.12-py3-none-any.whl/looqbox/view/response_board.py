from looqbox.render.abstract_render import BaseRender
from looqbox.objects.looq_object import LooqObject


class ResponseBoard(LooqObject):
    """
    Class that represents the response board object. It is used to have multiple response frames.
    """

    def __init__(self, content=None, action=None, dispose=None):
        """
        Args:
            content (list): List of content objects
            action (list): List of action objects
            dispose (str): Dispose of the response board
        
        Examples:
            >>> first_frame = lq.ResponseFrame([lq.ObjMessage("Hello World")])
            >>> second_frame = lq.ResponseFrame([lq.ObjMessage("Hello World 2")])
            >>> response_board = lq.ResponseBoard([first_frame, second_frame])
        """
        super().__init__()
        if action is None:
            action = []
        if content is None:
            content = []
        self.content = content
        self.action = action
        self.dispose = dispose

    def to_json_structure(self, visitor: BaseRender):
        return visitor.response_board_render(self)
