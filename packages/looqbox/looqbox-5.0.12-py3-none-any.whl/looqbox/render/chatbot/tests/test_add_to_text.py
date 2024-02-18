from looqbox.render.chatbot.base_chatbot_render import BaseChatbotRender
import unittest


class TestAddToText(unittest.TestCase):
    def setUp(self):
        self.renderer = BaseChatbotRender()

    def test_add_to_text_with_str(self):
        result = self.renderer.add_to_text("Hello", " World")
        self.assertEqual("HelloWorld", result)

    def test_add_to_text_with_empty_str(self):
        result = self.renderer.add_to_text("Hello", "")
        self.assertEqual("Hello", result)

    def test_add_to_text_with_none(self):
        result = self.renderer.add_to_text("Hello", None)
        self.assertEqual("Hello", result)

    def test_add_to_text_with_list(self):
        result = self.renderer.add_to_text("Hello", [" ", "World"])
        self.assertEqual("HelloWorld", result)

    def test_add_to_text_with_dict(self):
        result = self.renderer.add_to_text("Hello", {"text": "World"})
        self.assertEqual("HelloWorld", result)

    def test_add_to_text_with_dict_and_target(self):
        result = self.renderer.add_to_text("Hello", {"text": " World", "target": "example"})
        self.assertEqual("Hello", result)
        self.assertEqual([{"text": " World", "target": "example"}], self.renderer.non_text_objects)

    def test_add_to_text_with_dict_and_children(self):
        result = self.renderer.add_to_text("Hello", {"children": [" ", "World"], "separator": " "})
        self.assertEqual("Hello World", result)

    def test_add_to_text_with_complex_dict(self):
        result = self.renderer.add_to_text("Hello", {"children": [{"text": " World"}], "separator": " "})
        self.assertEqual("Hello World", result)

    def test_add_to_text_with_nested_list(self):
        result = self.renderer.add_to_text("Hello", [[" ", "World"]])
        self.assertEqual("HelloWorld", result)

    def test_add_to_text_with_multiple_elements_in_list(self):
        result = self.renderer.add_to_text("Hello", [" ", {"text": "World"}])
        self.assertEqual("HelloWorld", result)

    def test_add_to_text_with_empty_dict(self):
        result = self.renderer.add_to_text("Hello", {})
        self.assertEqual("Hello", result)

    def test_add_to_text_with_dict_no_text(self):
        result = self.renderer.add_to_text("Hello", {"not_text": " World"})
        self.assertEqual("Hello", result)

    def test_add_to_text_with_dict_and_uri(self):
        result = self.renderer.add_to_text("Hello", {"text": " World", "uri": "example"})
        self.assertEqual("Hello", result)
        self.assertEqual([{"text": " World", "uri": "example"}], self.renderer.non_text_objects)


if __name__ == '__main__':
    unittest.main()
