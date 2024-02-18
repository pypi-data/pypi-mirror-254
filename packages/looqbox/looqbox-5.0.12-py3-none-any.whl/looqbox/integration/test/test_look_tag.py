import unittest

from looqbox.integration.integration_links import look_tag
from looqbox.integration.test.nlp_test_helper import set_nlp_values


class TestLookTag(unittest.TestCase):

    def setUp(self) -> None:
        self.par_v1 = {
            "originalQuestion": "teste",
            "cleanQuestion": "teste",
            "residualQuestion": "",
            "residualWords": [""],
            "entityDictionary": None,
            "userlogin": "user",
            "userId": 666,
            "companyId": 0,
            "userGroupId": 0,
            "language": "pt-br",
            "$date": [
                [
                    "2019-01-08",
                    "2019-01-08"
                ]
            ],
            "$datetime": [
                [
                    "2019-01-08 00:00:00",
                    "2019-01-08 00:00:00"
                ]
            ],
            "$store": [1, 2, 3, 4, 5, 6, 7, 8],
            "apiVersion": 1
        }

        self.par_v2 = {
            "question": {
                "residualWords": [
                    "meta",
                    "python"
                ],
                "original": "meta python $debug",
                "clean": "meta python",
                "residual": "meta python"
            },
            "user": {
                "id": 1101,
                "login": "matheus",
                "groupId": 1,
                "language": "pt-br"
            },
            "entities": {
                "$store": {
                    "content": [
                        {
                            "segment": "da loja sao paulo",
                            "value": [
                                1
                            ]
                        }
                    ]
                },
                "$date": {
                    "content": [
                        {
                            "segment": "hoje",
                            "text": "hoje",
                            "value": [
                                [
                                    "2020-01-22",
                                    "2020-01-22"
                                ]
                            ]
                        }
                    ]
                }
            },
            "partitions": {

            },
            "companyId": 0,
            "apiVersion": 3,
            "keywords": [
                "meta",
                "python"
            ]
        }

        self.deprecation_warnings = False

    def test_look_tag_json_exception(self):
        """
        Test look_tag function with one entity in language version 2, this should raise an error
        """

        par = self.par_v2

        with self.assertRaises(Exception):
            look_tag("$date", par, _deprecated=self.deprecation_warnings)

    def test_look_tag(self):
        """
        Test look_tag function with multiple entities in language version 2
        """
        par = set_nlp_values("venda_esse_mes_nas_lojas_1_e_2.json")

        date = look_tag("$date", par, _deprecated=self.deprecation_warnings)
        self.assertEqual([['2023-11-01', '2023-12-01']], date)

        mix_entities = look_tag(["$date", "$loja"], par, _deprecated=self.deprecation_warnings)
        self.assertEqual([
            [['2023-11-01', '2023-12-01']],
            [1, 2]
        ], mix_entities)

