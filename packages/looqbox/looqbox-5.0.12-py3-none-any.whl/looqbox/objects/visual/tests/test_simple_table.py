import os
import unittest

import pandas as pd

from looqbox.objects.visual.looq_simple_table import ObjSimpleTable


class TestObjSimpleTable(unittest.TestCase):

    def setUp(self):
        self.obj_simple_table = ObjSimpleTable()
        self.metadata = {"CODE": "integer", "LABEL": "string"}
        self.obj_simple_table.metadata = self.metadata

        filepath = os.path.join(os.path.dirname(__file__), "reference", "simple_table")

        self.kwargs = dict(
            file_extension="csv",
            file_path=filepath,
            encoding="utf-8",
            index=False,
            sep=";"
        )

        self.sample = pd.DataFrame(
            {"CODE": [1, 2, 3], "LABEL": ["Baratinho", "Bem Bom", "Ki Barato"]})
        self.with_latin1_char = pd.DataFrame(
            {"CODE": [1, 2, 3], "LABEL": ["Só Açaí", "Descontão", "Ki preço"]})
        self.with_comma = pd.DataFrame(
            {"CODE": [1, 2, 3], "LABEL": ["Açaí com paçoca", "Pneu R$15,00", "Ki,, preço"]})
        self.with_semicolon = pd.DataFrame(
            {"CODE": [1, 2, 3], "LABEL": ["Açaí com paçoca", "Pneu R$15,00", "Ki; preço"]})
        self.with_single_quote = pd.DataFrame(
            {"CODE": [1, 2, 3], "LABEL": ["Spray automotivo", "Pneu 15'", "Roda aro 19''"]})
        self.with_double_quote = pd.DataFrame(
            {"CODE": [1, 2, 3], "LABEL": ['Spray automotivo', 'Pneu 15"', 'Roda aro 19""']}
        )

    def test_save_as_csv(self):
        self.obj_simple_table.data = self.sample
        self.obj_simple_table.save_as(
            file_name="sample",
            **self.kwargs
        )

    def test_save_as_csv_with_latin1_char(self):
        self.obj_simple_table.data = self.with_latin1_char
        self.obj_simple_table.save_as(
            file_name="with_latin1_char",
            **self.kwargs
        )

    def test_save_as_csv_with_comma(self):
        self.obj_simple_table.data = self.with_comma
        self.obj_simple_table.save_as(
            file_name="with_comma",
            **self.kwargs
        )

    def test_save_as_csv_with_semicolon(self):
        self.obj_simple_table.data = self.with_semicolon
        self.obj_simple_table.save_as(
            file_name="with_semicolon",
            **self.kwargs
        )

    def test_save_as_csv_with_single_quote(self):
        self.obj_simple_table.data = self.with_single_quote
        self.obj_simple_table.save_as(
            file_name="with_single_quote",
            **self.kwargs
        )

    def test_save_as_csv_with_double_quote(self):
        self.obj_simple_table.data = self.with_double_quote
        self.obj_simple_table.save_as(
            file_name="with_double_quote",
            **self.kwargs
        )



if __name__ == '__main__':
    unittest.main()
