import os
import unittest

from looqbox import load_json_from_path, ObjectMapper
from looqbox.objects.response_parameters.condition.set_relation import SetRelation


class TestSetRelation(unittest.TestCase):

    def setUp(self):
        self.current_dir = os.path.dirname(__file__)
        self.not_in_store = ObjectMapper.map(
            load_json_from_path(os.path.join(os.path.dirname(__file__), "resources", "set_relation.json")),
            SetRelation
        )

    def test_sql_filter_method(self):
        self.assertEqual(
            "AND ID_LOJA not in (1)",
            self.not_in_store.as_sql_filter("ID_LOJA")
        )
