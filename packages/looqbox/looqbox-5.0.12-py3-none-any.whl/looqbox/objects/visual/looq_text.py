import json
from multimethod import overload
from looqbox.objects.component_utility.css_option import CssOption as css
from looqbox.objects.visual.abstract_visual_component import AbstractVisualComponent
from looqbox.render.abstract_render import BaseRender
from looqbox.utils.utils import open_file
import os


class ObjText(AbstractVisualComponent):
    """
    Represents a visual component object for text with style properties.
    """

    def __init__(self, text, **properties):
        """
        Args:
            text (str): The main content of the text object.
            css_options (list , optional): A list of CSS options to change the text style.
        
        Examples:
            >>> example_text = ObjText("Sample Text")

            >>> from looqbox import CssOption as Css # CssOption is a class that contains all the CSS options available
            >>> example_styled_text = ObjText("Sample Text", css_options=[Css.FontSize(20), Css.Color("red")])
        """
        super().__init__(**properties)
        self.text = text
        self.value = text
        self._get_default_style()
        self._set_default_text_css_options()

    def _get_default_style(self) -> None:
        style_configuration_file = open_file(os.path.dirname(__file__), "..", "..", "resources", "default_style.json")

        self.default_style = json.load(style_configuration_file).get(self.__class__.__name__)
        style_configuration_file.close()

    def _set_default_text_css_options(self) -> None:

        if css.FontSize not in self.css_options:
            self.css_options = css.add(self.css_options, css.FontSize(self.default_style.get("fontSize")))

    def _set_title_css_options(self, level) -> dict:
        titles_options = {
            "fontSize": css.FontSize(self.default_style.get("title").get(level).get("fontSize")),
            "fontWeight": css.FontWeight(self.default_style.get("title").get(level).get("FontWeight")),
            "color": css.Color(self.default_style.get("title").get(level).get("Color"))
        }

        return titles_options

    def set_as_title(self, title_level: int | str = 1):
        """
        Method to set a given text as title, using HTML's header tag properties.

        Args:
            title_level (int | str, optional): Header level, could be assigned as an integer or the tag name.

        Examples:
            >>> example_title.set_as_title(1)
            >>> # or
            >>> example_title.set_as_title("H1")
            # in this case, both methods call will set the text property as an equivalent of <h1></h1> tag
        """

        title_properties = self._get_title_level_properties(title_level)

        self.css_options = css.clear(self.css_options, [css.FontSize, css.FontWeight, css.Color])

        self.css_options = css.add(self.css_options, title_properties.get("fontSize"))
        self.css_options = css.add(self.css_options, title_properties.get("fontWeight"))
        self.css_options = css.add(self.css_options, title_properties.get("color"))
        return self

    @overload
    def _get_title_level_properties(self, level: int) -> dict:
        level = "h" + str(level)
        properties = self._set_title_css_options(level)
        return properties

    @overload
    def _get_title_level_properties(self, level: str) -> dict:
        properties = self._set_title_css_options(level)
        return properties

    @property
    def set_text_alignment_left(self):
        self.css_options = css.add(self.css_options, css.TextAlign.left)
        return self

    @property
    def set_text_alignment_center(self):
        self.css_options = css.add(self.css_options, css.TextAlign.center)
        return self

    @property
    def set_text_alignment_right(self):
        self.css_options = css.add(self.css_options, css.TextAlign.right)
        return self

    def to_json_structure(self, visitor: BaseRender):
        return visitor.text_render(self)

    def __repr__(self):
        return f"{self.text}"
