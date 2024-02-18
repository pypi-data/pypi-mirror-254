from looqbox.render.abstract_render import BaseRender
from looqbox.objects.looq_object import LooqObject


class ObjFileUpload(LooqObject):
    """
    Creates a view to drag and drop a file that will be read and used in other script of the response.
    """
    def __init__(self, filepath, title=None, content=None, tab_label=None, value=None):
        """
        Args:
            filepath (str): Path where file will be upload to.
            title (str, optional): Title of the dropzone. Defaults to None.
            content (str, optional): Content that will be send to the other script. Defaults to None.

        Examples:
            >>> upload = ObjFileUpload(filepath="secondScript", title="Looq File Upload")
        """
        super().__init__()
        if title is None:
            title = []
        if content is None:
            content = []
        self.filepath = filepath
        self.title = title
        self.content = content
        self.tab_label = tab_label
        self.value = value

    def to_json_structure(self, visitor: BaseRender):
        return visitor.file_upload_render(self)
