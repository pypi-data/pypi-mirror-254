from looqbox.render.abstract_render import BaseRender
from looqbox.objects.looq_object import LooqObject


class ObjImageCapture(LooqObject):
    """
    Creates a looqbox image object from a webcam picture.
    """
    def __init__(self, filepath, title=None, content=None, value=None):
        """
        Args:
            filepath (str): Path for the script to which the image is returned.
            title (str, optional): Title of the image box.
            content (dict, optional): Format that the captured image data will be sent to the interface.

        Examples:
            >>> image = ObjImageCapture(filepath="filePath", title="Captura de Imagem")
        """
        super().__init__()
        if content is None:
            content = []
        if title is None:
            title = ""
        self.filepath = filepath
        self.title = title
        self.content = content
        self.value = value

    def to_json_structure(self, visitor: BaseRender):
        return visitor.image_capture_render(self)
