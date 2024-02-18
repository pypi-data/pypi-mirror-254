import json
import os
import unittest

import pandas as pd

from looqbox.objects.visual.table_body import TableBody
from looqbox.render.looqbox.base_looqbox_render import BrowserRender
from looqbox.utils.utils import load_json_from_path


class TestTableBody(unittest.TestCase):

    def setUp(self):

        self.maxDiff = None

        expected_json_path = os.path.join(
            os.path.dirname(__file__), "reference", "looq_table", "sales_with_drill.json")

        self.visitor = BrowserRender()
        self.expected_json = load_json_from_path(expected_json_path)
        self.table_body = TableBody(
            col_class={},
            col_format={'TM': 'number:2', 'Tickets': 'number:0', 'venda': 'number:0'},
            col_hierarchy=[],
            col_link={},
            col_range=None,
            col_style={},
            col_tooltip={},
            collapsable=False,
            collapse_hide_duplicates=True,
            table_content=pd.DataFrame({'Estado': {0: 'SP', 1: 'RJ', 2: 'MG', 3: 'SC', 4: 'AC', 5: 'PA'}, 'venda': {0: 2733461.535960132, 1: 802266.1575248649, 2: 628560.6376424839, 3: 567637.11397996, 4: 536355.176060435, 5: 305106.915459822}, 'TM': {0: 261.32519464246, 1: 271.1274611439219, 2: 290.46240186806097, 3: 222.69011925459395, 4: 319.4491816917421, 5: 382.81921638622583}, 'Tickets': {0: 10460, 1: 2959, 2: 2164, 3: 2549, 4: 1679, 5: 797}}),
            drill_text={},
            null_as='-',
            render_body=None,
            row_class={},
            row_format={},
            row_hierarchy=[],
            row_link={},
            row_range=None,
            row_style={},
            row_tooltip={},
            total_collapse=({}, ),
            value_class={},
            value_format={},
            value_link={'Estado': [[{'text': 'Ficha estado', 'link': 'Ficha estado [SP]'}, {'text': 'Ficha estado', 'link': 'Ficha estado [RJ]'}, {'text': 'Ficha estado', 'link': 'Ficha estado [MG]'}, {'text': 'Ficha estado', 'link': 'Ficha estado [SC]'}, {'text': 'Ficha estado', 'link': 'Ficha estado [AC]'}, {'text': 'Ficha estado', 'link': 'Ficha estado [PA]'}], [{'text': 'por cidade', 'link': 'venda $script ontem estado [SP] por cidade'}, {'text': 'por cidade', 'link': 'venda $script ontem estado [RJ] por cidade'}, {'text': 'por cidade', 'link': 'venda $script ontem estado [MG] por cidade'}, {'text': 'por cidade', 'link': 'venda $script ontem estado [SC] por cidade'}, {'text': 'por cidade', 'link': 'venda $script ontem estado [AC] por cidade'}, {'text': 'por cidade', 'link': 'venda $script ontem estado [PA] por cidade'}], [{'text': 'por loja', 'link': 'venda $script ontem estado [SP] por loja'}, {'text': 'por loja', 'link': 'venda $script ontem estado [RJ] por loja'}, {'text': 'por loja', 'link': 'venda $script ontem estado [MG] por loja'}, {'text': 'por loja', 'link': 'venda $script ontem estado [SC] por loja'}, {'text': 'por loja', 'link': 'venda $script ontem estado [AC] por loja'}, {'text': 'por loja', 'link': 'venda $script ontem estado [PA] por loja'}], [{'text': 'por categoria', 'link': 'venda $script ontem estado [SP] por categoria'}, {'text': 'por categoria', 'link': 'venda $script ontem estado [RJ] por categoria'}, {'text': 'por categoria', 'link': 'venda $script ontem estado [MG] por categoria'}, {'text': 'por categoria', 'link': 'venda $script ontem estado [SC] por categoria'}, {'text': 'por categoria', 'link': 'venda $script ontem estado [AC] por categoria'}, {'text': 'por categoria', 'link': 'venda $script ontem estado [PA] por categoria'}], [{'text': 'por subcategoria', 'link': 'venda $script ontem estado [SP] por subcategoria'}, {'text': 'por subcategoria', 'link': 'venda $script ontem estado [RJ] por subcategoria'}, {'text': 'por subcategoria', 'link': 'venda $script ontem estado [MG] por subcategoria'}, {'text': 'por subcategoria', 'link': 'venda $script ontem estado [SC] por subcategoria'}, {'text': 'por subcategoria', 'link': 'venda $script ontem estado [AC] por subcategoria'}, {'text': 'por subcategoria', 'link': 'venda $script ontem estado [PA] por subcategoria'}], [{'text': 'por plu', 'link': 'venda $script ontem estado [SP] por plu'}, {'text': 'por plu', 'link': 'venda $script ontem estado [RJ] por plu'}, {'text': 'por plu', 'link': 'venda $script ontem estado [MG] por plu'}, {'text': 'por plu', 'link': 'venda $script ontem estado [SC] por plu'}, {'text': 'por plu', 'link': 'venda $script ontem estado [AC] por plu'}, {'text': 'por plu', 'link': 'venda $script ontem estado [PA] por plu'}]]},
            value_style={},
            value_tooltip={}
        )

    def test_json_structure(self):

        result = remove_empty_values_deep(self.table_body.to_json_structure(self.visitor))
        expected_body = self.expected_json["content"][0]["content"][0]["body"]

        self.assertDictEqual(result, expected_body)



# Helper functions
def remove_empty_values(data):
    if isinstance(data, dict):
        return {key: remove_empty_values(value)
                for key, value in data.items()
                if value or isinstance(value, (int, float, bool))}
    elif isinstance(data, list):
        return [remove_empty_values(item) for item in data if item or isinstance(item, (int, float, bool))]
    else:
        return convert_tuples_to_lists(data)

def remove_empty_values_deep(data):
    data = remove_empty_values(data)
    return convert_ints_to_floats(remove_empty_values(data))

def convert_tuples_to_lists(data):
    if isinstance(data, tuple):
        return [convert_tuples_to_lists(item) for item in data]
    elif isinstance(data, list):
        return [convert_tuples_to_lists(item) for item in data]
    elif isinstance(data, dict):
        return {key: convert_tuples_to_lists(value) for key, value in data.items()}
    else:
        return data

def convert_ints_to_floats(data):
    if isinstance(data, int):
        return float(data)
    elif isinstance(data, (list, tuple)):
        return [convert_ints_to_floats(item) for item in data]
    elif isinstance(data, dict):
        return {key: convert_ints_to_floats(value) for key, value in data.items()}
    else:
        return data


if __name__ == "__main__":
    unittest.main()

