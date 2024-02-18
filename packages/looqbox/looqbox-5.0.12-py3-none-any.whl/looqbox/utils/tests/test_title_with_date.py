import os
import unittest

from looqbox import ObjectMapper
from looqbox.objects.response_parameters.condition.temporal_relation import TemporalRelation
from looqbox.utils.utils import title_with_date, load_json_from_path


class TestTitleWithDateFunction(unittest.TestCase):

    def setUp(self):
        self.current_dir = os.path.dirname(__file__)
        self.month_temporal_relation = ObjectMapper.map(
            load_json_from_path(
                os.path.join(
                    os.path.dirname(__file__),
                    "..", "..", "objects", "response_parameters", "tests", "resources", "month_temporal_relation.json"
                )
            ), TemporalRelation
        )

        self.year_temporal_relation = ObjectMapper.map(
            load_json_from_path(
                os.path.join(
                    os.path.dirname(__file__),
                    "..", "..", "objects", "response_parameters", "tests", "resources", "year_temporal_relation.json"
                )
            ), TemporalRelation
        )

    def test_simple_date(self):
        result = title_with_date("Período", ["2022-01-01", "2022-01-01"], "pt-br")
        self.assertEqual(result, "Período dia 01/01/2022 (sab sem: 52/2022)")
    def test_date_interval(self):
        result = title_with_date("Período", ["2022-01-01", "2022-01-02"], "pt-br")
        self.assertEqual(result, "Período de 01/01/2022 a 02/01/2022")

    def test_month_title(self):
        result = title_with_date("Período", ["2023-12-01", "2023-12-31"], "pt-br")
        self.assertEqual(result, "Período de 01/12/2023 a 31/12/2023 (mês: 12/2023)")

    def test_week_title(self):
        result = title_with_date("Período", ["2023-12-04", "2023-12-10"], "pt-br")
        self.assertEqual(result, "Período de 04/12/2023 a 10/12/2023 (sem: 49 - 2023)")

    def test_year_title(self):
        result = title_with_date("Período", ["2023-01-01", "2023-12-31"], "pt-br")
        self.assertEqual(result, "Período de 01/01/2023 a 31/12/2023 (ano: 2023)")
    def test_simple_datetime(self):
        result = title_with_date("Período", ["2022-01-01 12:00:00", "2022-01-01 12:00:00"], "pt-br")
        self.assertEqual(result, "Período dia 01/01/2022 12:00:00 (sab sem: 52/2022)")
    def test_datetime_interval(self):
        result = title_with_date("Período", ["2022-01-01 12:00:00", "2022-01-02 13:00:00"], "pt-br")
        self.assertEqual(result, "Período de 01/01/2022 12:00:00 a 02/01/2022 13:00:00")
    def test_open_date_interval(self):
        result = title_with_date("Período", ["2022-01-01", None], "pt-br")
        self.assertEqual(result, "Período a partir de 01/01/2022")
    def test_open_datetime_interval(self):
        result = title_with_date("Período", ["2022-01-01 12:00:00", None], "pt-br")
        self.assertEqual(result, "Período a partir de 01/01/2022 12:00:00")
    def test_end_open_date_interval(self):
        result = title_with_date("Período", [None, "2022-01-01"], "pt-br")
        self.assertEqual(result, "Período até 01/01/2022")
    def test_end_open_datetime_interval(self):
        result = title_with_date("Período", [None, "2022-01-01 12:00:00"], "pt-br")
        self.assertEqual(result, "Período até 01/01/2022 12:00:00")
    def test_title_generator_for_temporal_relation(self):
        result = title_with_date("Venda", self.month_temporal_relation, "pt-br")
        self.assertEqual(result, "Venda de 01/11/2023 00:00:00 a 30/11/2023 00:00:00 (mês: 11/2023)")

    def test_title_generator_for_year_temporal_relation(self):
        result = title_with_date("Venda", self.year_temporal_relation, "pt-br")
        self.assertEqual(result, "Venda de 01/01/2023 a 31/12/2023 (ano: 2023)")


if __name__ == '__main__':
    unittest.main()
