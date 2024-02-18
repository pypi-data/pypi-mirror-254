import unittest

from looqbox.integration.test.nlp_test_helper import set_nlp_values
from looqbox.integration.integration_links import get_partition


class TestGetPartition(unittest.TestCase):

    def test_get_partition(self):
        """
        Test get_partition function with one partition
        """
        par = set_nlp_values("venda_por_dia_esse_mes.json")

        date_json = get_partition("$date", par)
        self.assertEqual([
            {"segment": "por dia", "text": "por dia", "value": ["byDay"]}
        ], date_json)

        default_value = get_partition("$undefined", par)
        self.assertIsNone(default_value)

    def test_get_partition_for_multiple_partitions(self):
        """
        Test get_partition function with multiple partitions
        """
        par = set_nlp_values("venda_por_loja_por_dia.json")

        mix_entities = get_partition(["$date", "$loja"], par)
        self.assertEqual([
            [{"segment": "por dia", "text": "por dia", "value": ["byDay"]}],
            [{"segment": "por loja", "text": "por loja", "value": []}]
        ], mix_entities)

    def test_list_none_diff(self):
        par = set_nlp_values("venda_esse_ano_por_mes_por_estado.json")

        state = get_partition("$estado", par, only_value=True)
        self.assertEqual([], state)

    def test_type_check_only_values(self):
        par = set_nlp_values("venda_esse_ano_por_mes_por_estado.json")
        partiton_value = get_partition("NoPartition", par, partition_default=None, only_value=True)
        self.assertIsNone(partiton_value)

