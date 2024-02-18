import os

from pandas import DataFrame

from looqbox.global_calling import GlobalCalling
from looqbox.objects.api import ObjMessage
from looqbox.objects.looq_object import LooqObject
from looqbox.render.abstract_render import BaseRender


class ObjSimpleTable(LooqObject):
    """
    A class used to create a table with minimal information.
    """

    def __init__(self,
                 data: DataFrame = None,
                 metadata: dict = None,
                 rows: int = None,
                 null_as: int or str = None,
                 searchable: bool = False,
                 sortable: bool = False,
                 pagination: int = 20,
                 title: list | None = None,
                 name: str = "objSimpleTable"):
        """
        Args:
            data (pandas.DataFrame, optional): The content of the table. Defaults to None.
            metadata (dict, optional): The metadata retrieved from a query. Defaults to None (empty dictionary).
            rows (int, optional): The number of rows. If not provided and data is not None, it will be the number of 
                                  entries in data. Defaults to None.
            null_as (int or str, optional): The value to replace None or NaN cells with. Defaults to '-'.
            searchable (bool, optional): Whether the table is searchable. Defaults to False.
            sortable (bool, optional): Whether the table is sortable. Defaults to False.
            pagination (int, optional): The number of entries to show in a page when pagination is used.
                                        Defaults to 20.
            title (list, optional): A list of strings to set as the table title(s). Defaults to None (empty list).
            name (str, optional): The object's name. Defaults to "objSimpleTable".

        Example:
            >>> obj_simple_table = ObjSimpleTable(data=pandas.DataFrame({'column_1': [1, 2, 3]}), 
            >>>     metadata={"column_1": "integer"}, rows=3, null_as="-", 
            >>>     searchable=False, sortable=False, 
            >>>     pagination=20, title=["Table Title"], 
            >>>     name= "objSimpleTable")
        """
        super().__init__()

        metadata = metadata or dict()
        null_as = null_as or "-"

        self.data = data
        self.name = name
        self.metadata = metadata
        self.rows = rows
        if self.rows is None and self.data is not None:
            self.rows = self.data.shape[0]
        self.null_as = null_as

        self.total = None
        self.searchable = searchable
        self.sortable = sortable
        self.pagination = pagination
        self.title = title or []

    def to_json_structure(self, visitor: BaseRender):
        return visitor.simple_table_render(self)

    @staticmethod
    def head_element_to_json(column, metadata):
        element = {
            "title": column,
            "dataIndex": column,
            "metadata": metadata.get(column)
        }

        return element

    def build_head_content(self, table_data, metadata):
        return [self.head_element_to_json(column, metadata) for column in table_data]

    @staticmethod
    def build_body_content(table_data):
        return table_data.to_dict('records')

    def save_as(self, file_name: str, file_extension: str = "csv", file_path: str = None, dropna=True, **kwargs) -> ObjMessage:
        """
        Save the ObjSimpleTable's data as a file.

        Args:
            file_name (str): The name of the file to be saved.
            file_extension (str, optional): The extension of the file. Can be:
                                            .csv: Comma-separated values.
                                            .xlsx: Excel sheet.
                                            .json: JSON string.
                                            .txt: Tabular text.
                                            .xml: XML document.
                                            Defaults to "csv".
            file_path (str, optional): The path where the file should be saved. If None, the file will be saved 
                                       in the "entity_sync_path" from the looq object. Defaults to None.
            dropna (bool, optional): Whether to omit missing values from dataset. Defaults to True.
            **kwargs: Arbitrary keyword arguments that will be passed to the chosen pandas data saving function.

        Returns:
            ObjMessage: An ObjMessage instance.

        Example:
            obj_simple_table.save_as(file_name='table', file_extension='csv',
                                     file_path='/path/to/save', dropna=True)
        """

        if file_path is None:
            file_path = GlobalCalling.looq.entity_sync_path or ""

        if file_extension[0] != ".":
            file_extension = "." + file_extension

        file_path_with_name = os.path.join(
            file_path,
            file_name + file_extension
        )

        save_function_map = {
            ".csv": "to_csv({}, **kwargs)",
            ".xlsx": "to_excel({}, **kwargs)",
            ".json": "to_json({}, **kwargs)",
            ".txt": "to_string({}, **kwargs)",
            ".xml": "to_xml({}, **kwargs)"
        }

        function_args = '"{}"'.format(file_path_with_name)
        save_function = save_function_map.get(file_extension).format(function_args)

        save_function = "self.data." + save_function
        if dropna:
            self._remove_empty_values_from_dataset()
        # self.data = escape_characters_in_pandas_dataframe(self.data)
        exec(save_function)
        # replace_double_double_quotes_on_csv(file_path_with_name, n_cols=len(self.data.columns))

        return ObjMessage(file_name + file_extension, type="success")

    def _remove_empty_values_from_dataset(self):
        from numpy import nan
        self.data.replace('', nan, inplace=True)
        self.data.dropna(inplace=True)


def escape_characters_in_pandas_dataframe(dataframe: DataFrame, characters_to_escape: dict = None):
    """
    Escape characters in a Pandas Dataframe.

    Args:
        dataframe (DataFrame): The dataframe to escape characters in.
        characters_to_escape (dict, optional): The characters to escape from the dataframe. Defaults to a dictionary
                                               with ";" being replaced by "\;" and '"' being replaced by '\"'.

    Returns:
        DataFrame: The escaped dataframe.

    Example:
        my_dataframe = pandas.DataFrame({"column_1": ['"John', ";;Doe;;", "48"]})
        escaped_dataframe = escape_characters_in_pandas_dataframe(my_dataframe)
    """

    if not characters_to_escape:
        characters_to_escape = {
            '"': r'\"',
            ';': r'\;'
        }

    for column in dataframe.columns:
        escaped_values = []
        for value in dataframe[column].values:
            if isinstance(value, str):
                value = value.translate(str.maketrans(characters_to_escape))
            escaped_values.append(value)
        dataframe[column] = escaped_values

    return dataframe


def replace_double_double_quotes_on_csv(filename: str, n_cols: int = None):
    """
    Replace double double quotes on a CSV file.

    Args:
        filename (str): The filename of the csv file to replace the double double quotes.

    Example:
        replace_double_double_quotes_on_csv("/path/to/myfile.csv")
    """

    # with open(filename, 'r', encoding='utf-8') as file:
    #     lines = file.readlines()
    #     file.close()
    #
    # with open(filename, 'w', encoding='utf-8') as file:
    #     for line in lines:
    #         fields = line.split(',')
    #         if len(fields) == n_cols:
    #             file.write(line)
