import unittest

from looqbox.integration.integration_links import get_entity
from looqbox.integration.test.nlp_test_helper import set_nlp_values
from looqbox.objects.response_parameters.token import Token


class TestGetEntity(unittest.TestCase):

    def test_get_entity(self):
        """
        Test get_entity function with one entity
        """
        par = set_nlp_values("venda_esse_mes_nas_lojas_1_e_2.json")

        date = get_entity("$date", par)
        self.assertEqual(
            [{
                'entity_name': '$date',
                'segment': 'esse mes',
                'text': 'esse mes',
                'value': [['2023-11-01', '2023-12-01']]
            }], date)

        default_value = get_entity("$undefined", par)
        self.assertIsNone(default_value)

    def test_get_entity_for_multiple_entities(self):
        """
        Test get_entity function with multiple entities
        """
        par = set_nlp_values("venda_esse_mes_nas_lojas_1_e_2.json")

        mix_entities = get_entity(["$date", "$loja"], par)
        self.assertEqual([
            [{
                'entity_name': '$date',
                'segment': 'esse mes',
                'text': 'esse mes',
                'value': [['2023-11-01', '2023-12-01']]
            }],
            [{'segment': 'lojas 1 2', 'text': 'lojas 1 2', 'value': [1, 2]}]], mix_entities)

    def test_comparative_entity(self):
        par = set_nlp_values("venda_ontem_vs_hj.json")

        comparative = get_entity("$comparative", par)
        model_comparative = [{'segment': 'ontem vs hj', 'text': 'ontem vs hj', 'value': [
            {'segment': 'ontem', 'text': 'ontem', 'value': [['2023-11-06 00:00:00', '2023-11-07 00:00:00']],
             'entity_name': '$datetime'},
            {'segment': 'hj', 'text': 'hj', 'value': [['2023-11-07 00:00:00', '2023-11-08 00:00:00']],
             'entity_name': '$datetime'}], 'entity_name': '$datetime'}]



        self.assertEqual(model_comparative, comparative)

    def test_get_entity_only_value(self):
        """
        Test get_entity function with only_value set to True
        """
        par = set_nlp_values("venda_esse_mes_nas_lojas_1_e_2.json")

        date_value = get_entity("$date", par, only_value=True)
        self.assertEqual([['2023-11-01', '2023-12-01']], date_value)

        store_value = get_entity("$loja", par, only_value=True)
        self.assertEqual([1, 2], store_value)

        default_value = get_entity("$undefined", par, only_value=True)
        self.assertIsNone(default_value)

    def test_get_entity_for_multiple_entities_with_only_value(self):
        """
        Test get_entity function with multiple entities and only_value set to True
        """
        par = set_nlp_values("venda_esse_mes_nas_lojas_1_e_2.json")

        mix_value = get_entity(["$date", "$loja"], par, only_value=True)
        self.assertEqual([[['2023-11-01', '2023-12-01']], [1, 2]], mix_value)

    def test_comparative_entity_with_only_value(self):
        par = set_nlp_values("venda_ontem_vs_hj.json")

        comparative = get_entity("$comparative", par, only_value=True)
        self.assertEqual([
            [
                ['2023-11-06 00:00:00', '2023-11-07 00:00:00'], ['2023-11-07 00:00:00', '2023-11-08 00:00:00']
            ]
        ], comparative)

    def test_get_entity_for_date_on_datetime_language_output(self):
        """
        Test get_entity function with date and datetime entities
        Since Language version 3+ does not differentiate date and datetime, both $date and $datetime
        should return it´s respective values using the same class
        """
        par = set_nlp_values("venda_hoje_as_12h.json")

        date = get_entity("$date", par)
        self.assertEqual([
            {
                'entity_name': '$date',
                'segment': 'hoje as 12h',
                'text': 'hoje as 12h',
                'value': [['2023-11-23', '2023-11-23']]
            }
        ], date)

    def test_get_entity_for_datetime(self):
        par = set_nlp_values("venda_hoje_as_12h.json")

        datetime = get_entity("$datetime", par)
        self.assertEqual([
            {
                'entity_name': '$datetime',
                'segment': 'hoje as 12h',
                'text': 'hoje as 12h',
                'value': [['2023-11-23 12:00:00', '2023-11-23 13:00:00']]
            }
        ], datetime)

    def test_get_entity_for_null_entities(self):
        par = set_nlp_values("venda_por_loja_por_dia.json")

        datetime = get_entity("$datetime", par)
        self.assertIsNone(datetime)

        date = get_entity("$date", par)
        self.assertIsNone(date)

    def test_rank(self):
        par = set_nlp_values("quais_5_lojas_mais_venderam.json")
        topn = get_entity("$topn", par, only_value=True)
        self.assertEqual(5, topn)

    def test_get_datetime_value(self):
        par = set_nlp_values("ultimos_15_min.json")
        datetime_value = get_entity("$datetime", par, only_value=True)
        self.assertEqual(
            [["2023-12-05 10:31:49", "2023-12-05 10:32:00"]],
            datetime_value
        )

    def test_non_condition_class_found(self):
        par = set_nlp_values("no_condition.json")
        date = get_entity("$date", par,  entity_default=[["2023-01-01", "2023-12-31"]] ,only_value=True)
        self.assertEqual([["2023-01-01", "2023-12-31"]], date)

    def test_type_check_only_values(self):
        par = set_nlp_values("no_condition.json")
        entity_value = get_entity("$NoEntity", par, entity_default=None, only_value=True)
        self.assertIsNone(entity_value)

    def test_get_entity_comparative_token(self):
        model_token = [Token(segment='loja 1 vs loja 2', text='loja 1 vs loja 2', id=None,
                             value=[Token(segment='loja 1', text='loja 1', id=None, value=[1], entity_name=None),
                                    Token(segment='loja 2', text='loja 2', id=None, value=[2], entity_name=None)],
                             entity_name=['$store'])]

        par = set_nlp_values("venda_loja1_vs_loja2.json")
        self.assertEqual(
           model_token,
            get_entity("$comparative", par,as_token=True)
        )

    def test_get_entity_comparative_same_entity_as_dict(self):


        model_dict = [{'entity_name': ['$store'], 'segment': 'loja 1 vs loja 2', 'text': 'loja 1 vs loja 2', 'value':
            [{'segment': 'loja 1', 'text': 'loja 1', 'value': [1]},
             {'segment': 'loja 2', 'text': 'loja 2', 'value': [2]}]}]

        par = set_nlp_values("venda_loja1_vs_loja2.json")
        self.assertEqual(
            model_dict,
            get_entity("$comparative", par, as_dict=True)
        )

    def test_get_entity_comparative_between_entities_as_dict(self):


        model_dict = [
            {
            'entity_name': ['$estado', '$store'],
            'segment': 'estado sp vs loja 1',
            'text': 'estado sp vs loja 1',
            'value': [{
                'segment': 'estado sp',
                'text': 'estado sp',
                'value': ['SP']},
                {
                    'segment': 'loja 1',
                    'text': 'loja 1',
                    'value': [1]
                }
            ]
          }
        ]

        par = set_nlp_values("venda_estado_vs_loja.json")
        self.assertEqual(
            model_dict,
            get_entity("$comparative", par, as_dict=True)
        )