import json
import unittest

from looqbox.utils.utils import _format_quotes


class TestFormatQuotes(unittest.TestCase):

    def test_middle_quote(self):
        input_string = '{"my_key": "{my"Text}"}'
        expected_result = '{"my_key": "{my\\"Text}"}'
        formatted_str = _format_quotes(input_string)
        assert json.loads(formatted_str)
        self.assertEqual(formatted_str, expected_result)

    def test_end_quote_escaped(self):
        input_string = '{"my_key": "{myText}\\"}'
        expected_result = '{"my_key": "{myText}"}'
        formatted_str = _format_quotes(input_string)
        assert json.loads(formatted_str)
        self.assertEqual(formatted_str, expected_result)

    def test_middle_quote_escaped(self):
        input_string = '{"my_key\\": "{myText}"}'
        expected_result = '{"my_key": "{myText}"}'
        formatted_str = _format_quotes(input_string)
        assert json.loads(formatted_str)
        self.assertEqual(formatted_str, expected_result)

    def test_end_quote_double_escaped(self):
        input_string = '{"my_key": "{myText}\\\\"}'
        expected_result = '{"my_key": "{myText}"}'
        formatted_str = _format_quotes(input_string)
        assert json.loads(formatted_str)
        self.assertEqual(formatted_str, expected_result)

    def test_double_lined_quote_escaped_json(self):
        input_string = """
        {
            "my_key": [
            "Pasta_Workforce_RW",
            "Time de Liderança Expansão\\\\"
            ]       
        }
        """
        expected_result = """
        {
            "my_key": [
            "Pasta_Workforce_RW",
            "Time de Liderança Expansão"
            ]       
        }
        """
        formatted_str = _format_quotes(input_string)
        assert json.loads(formatted_str)
        self.assertEqual(formatted_str, expected_result)


