import unittest

from looqbox.integration.test.nlp_test_helper import set_nlp_values
from looqbox.integration.integration_links import get_keyword


class TestGetKeywords(unittest.TestCase):
    # setup
    def setUp(self):
        self.par = set_nlp_values("venda_esse_ano_por_mes_por_estado.json")

    def test_get_one_keyword(self):
        self.assertEqual([{'segment': 'venda', 'text': 'venda', 'id': 5}], get_keyword("venda", self.par))

    def test_get_two_keywords_two_calls_with_only_value(self):
        venda = get_keyword("venda", self.par, only_value=True)
        tickets = get_keyword("tickets", self.par, only_value=True)
        self.assertEqual([5, 130], [venda, tickets])

    def test_get_two_keywords_one_call(self):
        self.assertEqual(
            [
                [{'segment': 'venda', 'text': 'venda', 'id': 5}],
                [{'segment': 'tickets', 'text': 'tickets', 'id': 130}]
            ],
            get_keyword(["venda", "tickets"], self.par)
        )

    def test_get_two_keywords_one_call_with_only_value(self):
        self.assertEqual([5, 130], get_keyword(["venda", "tickets"], self.par, only_value=True))

    def test_type_check_only_values(self):
        keyword_value = get_keyword("NoKeyword", self.par, keyword_default=None, only_value=True)
        self.assertIsNone(keyword_value)