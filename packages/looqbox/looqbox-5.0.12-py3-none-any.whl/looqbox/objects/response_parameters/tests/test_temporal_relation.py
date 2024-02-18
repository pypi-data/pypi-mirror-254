import os
import unittest

from looqbox import load_json_from_path, ObjectMapper
from looqbox.objects.response_parameters.condition.temporal_relation import TemporalRelation


class TestTemporalRelation(unittest.TestCase):

    def setUp(self):
        self.current_dir = os.path.dirname(__file__)
        self.month_temporal_relation = ObjectMapper.map(
            load_json_from_path(os.path.join(os.path.dirname(__file__), "resources", "month_temporal_relation.json")),
            TemporalRelation
        )
        self.hour_temporal_relation = ObjectMapper.map(
            load_json_from_path(os.path.join(os.path.dirname(__file__), "resources", "hour_temporal_relation.json")),
            TemporalRelation
        )

    def test_date_str_by_granularity(self):
        self.assertEqual(
            [['2023-11-01', '2023-11-30']],
            self.month_temporal_relation.date_str_by_granularity
        )
        self.assertEqual(
            [['2023-11-01 00:00:00', '2023-11-30 23:00:00']],
            self.hour_temporal_relation.date_str_by_granularity
        )

    def test_date_evaluated_boundaries(self):
        self.assertEqual(
            ['2023-11-01 00:00:00', '2023-11-30 00:00:00'],
            self.month_temporal_relation.date_with_evaluated_boundaries
        )
