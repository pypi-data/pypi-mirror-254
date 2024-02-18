import json
import os

from multipledispatch import dispatch

from looqbox.utils.utils import open_file
from looqbox.class_loader.class_loader import ClassLoader
from looqbox.database.database_exceptions import ConnectionTypeNotFound
from looqbox.database.connections.api import SqlThreadManager
from looqbox.database.connections.connection_base import BaseConnection
from looqbox.global_calling import GlobalCalling
from looqbox.objects.api import ObjTable

__all__ = ["sql_in", "sql_filter", "connect", "sql_execute", "sql_between", "sql_close", "sql_execute_parallel",
           "add_to_parallel_batch"]

query_parallel_batch = list()


@dispatch(str)
def connect(connection_name: str, parameter_as_json=False, use_all_jars=True, query_method="default") -> BaseConnection:
    """
    Execute a connection in a database.

    Args:
        connection_name (str): String with the database name
        parameter_as_json (bool): Set if the parameters will be in JSON format or not
        use_all_jars (bool): If set as True, the connection will import all available jars, allowing connection with
                                different database within the same JVM.
                                If this flag is set as False only the connection required jar will be loaded, thus the
                                connection is going to become prone to error, in case another database technology
                                (e.g. another driver, use another version for the same driver) is used, the Looqbox Kernel
                                will crash due the lack of the correct jar(s) file(s).
                                Therefore, setting use_all_jars as False is recommended for tests purpose or for an advanced
                                user.
        query_method (bool, optional): the method to perform the query regardless the database type.
    
    Examples:
        >>> connect("connection_name")
    """

    connection = _connection_factory(connection_name, parameter_as_json, use_all_jars, query_method)
    connection.connect()
    return connection


@dispatch(list)
def connect(connection_name: list, parameter_as_json=False, use_all_jars=True, query_method="default") -> list[BaseConnection]:
    """
    Execute a connection in a database.

    Args:
        connection_name (list): List of strings with the database name
        parameter_as_json (bool): Set if the parameters will be in JSON format or not
        use_all_jars (bool): If set as True, the connection will import all available jars, allowing connection with
                                different database within the same JVM.
                                If this flag is set as False only the connection required jar will be loaded, thus the
                                connection is going to become prone to error, in case another database technology
                                (e.g. another driver, use another version for the same driver) is used, the Looqbox Kernel
                                will crash due the lack of the correct jar(s) file(s).
                                Therefore, setting use_all_jars as False is recommended for tests purpose or for an advanced
                                user.
        query_method (bool, optional): the method to perform the query regardless the database type.
    
    Examples:
        >>> connect(["connection_name1", "connection_name2"])
    """
    # TODO marcar como deprecated
    connections = []
    for connection in connection_name:
        current_connection = _connection_factory(connection, parameter_as_json, use_all_jars)
        current_connection.connect()
        connections.append(current_connection)
    return connections


@dispatch(BaseConnection)
def connect(connection_name: BaseConnection,  query_method="default") -> BaseConnection:
    """
    Returned the connection that are already created.

    Args:
        connection_name (BaseConnection): ObjectConnection
        query_method (bool, optional): the method to perform the query regardless the database type.
    """
    return connection_name


def _get_connection_type(connection, parameter_as_json):
    """
        Get credentials for a list of connections.
        
        Args:
            connection (str | list): String or list of database names
            parameter_as_json (bool): Set if the parameters will be in JSON format or not
    """
    connection_credential = _get_connection_file()

    try:
        if not parameter_as_json:
            connection_credential = GlobalCalling.looq.connection_config[connection]
        else:
            connection_credential = connection_credential[connection]
    except:
        raise Exception(
            "Connection " + connection + " not found in the file " + GlobalCalling.looq.connection_file)
    return connection_credential.get("type", "").lower()


def _get_connection_file() -> dict:
    try:
        if isinstance(GlobalCalling.looq.connection_config, dict):
            file_connections = GlobalCalling.looq.connection_config
        else:
            file_connections = open(GlobalCalling.looq.connection_config)
            file_connections = json.load(file_connections)
    except FileNotFoundError:
        raise Exception("File connections.json not found")
    return file_connections


def _connection_factory(connection_name: str, parameter_as_json: bool,
                        use_all_jars: bool, query_method) -> BaseConnection:

    connection_type = _get_connection_type(connection_name, parameter_as_json=parameter_as_json)

    connection_configuration_file = open_file(os.path.dirname(__file__), "..", "resources", "connection_class_path.json")

    connections_factory = json.load(connection_configuration_file)

    if connection_type in connections_factory.keys():
        class_path, class_name = connections_factory[connection_type].get(query_method).rsplit(".", 1)
        conn = ClassLoader(class_name, class_path).load_class()
        return conn(connection_name,
                    parameter_as_json=parameter_as_json,
                    use_all_jars=use_all_jars)
    else:
        raise ConnectionTypeNotFound("\nConnection type is not supported")


def sql_execute(connection: str | BaseConnection, query, replace_parameters=None, close_connection=True,
                show_query=False, null_as=None, add_quotes=False, cache_time=None, optimize_for_large_datasets=False,
                use_query_caller=False):
    """
    Function to execute a query inside the connection informed. The result of the query will be
    transformed into a ObjTable to be used inside the response.

    Args:
        connection (str | BaseConnection): Connection name or object
        query (str | dict): sql script to query result set (in Big Query or JDBC database) in a string format.
                            For a MongoDB use in a dict format.
        replace_parameters (list, optional): List of parameters to be used in the query. These parameters will replace the numbers
                                   with `` in the query.
        close_connection (bool, optional): Define if automatically closes the connection. Default is True.
        show_query (bool, optional): Print the query in the console. Default is False.
        null_as (str, optional): Default value to fill null values in the result set. Default is None.
        add_quotes (bool, optional): Involves replaced parameters with quotes. Default is False.
        cache_time (int, optional): Time to leave of cache file in seconds, one might set up to 300 seconds. Default is None.
        optimize_for_large_datasets (bool, optional): Optimize the query execution for large datasets, this mode may present poor
    performance for smaller queries (currently only Big Query supports this mode). Default is False.
        use_query_caller (bool, optional): Set whether the Query Caller will be used in JDBC queries.

    Returns:
        lq.ObjTable: Object with the query result data.

    Examples:
        >>> # SQL
        >>> sql_query = "SELECT * FROM table_name"
        >>> sql_execute("sql_connection_name", sql_query)
        >>> 
        >>> # Mongo
        >>> mongo_query = {"collection": "example",
        >>>                "query": {"store":10},
        >>>                "fields": {"_id": 0, "name": 1, "sales": 1}
        >>>               }
        >>> sql_execute("mongo_connection_name", mongo_query)
    """

    query = _sql_replace_parameters(query, replace_parameters, add_quotes)

    print_query(query, show_query)

    query_dataframe = ObjTable(null_as=null_as)

    method = "query_caller" if use_query_caller else "default"

    connection = connect(connection, query_method=method)

    connection.set_query_script(query)

    connection.set_optimization_for_large_datasets(optimize_for_large_datasets)

    connection.execute(cache_time)

    query_dataframe.data = connection.retrieved_data

    query_dataframe = _count_rows_and_columns(query_dataframe)

    if close_connection:
        connection.close_connection()

    return query_dataframe


def _count_rows_and_columns(query_dataframe):
    query_dataframe.rows = query_dataframe.data.shape[0]
    query_dataframe.cols = query_dataframe.data.shape[1]
    return query_dataframe


def print_query(query, show_query):
    test_mode = GlobalCalling.looq.test_mode

    if show_query and test_mode:
        print(query)


def _sql_replace_parameters(query, replace_parameters, replace_with_quotes=False):
    """
    Replaces parameters in a SQL query.

    Args:
        query (str): Query to be changed.
        replace_parameters (List[Union[str, int, float]]): Values to substitute.
        replace_with_quotes (bool, optional): Encloses replaced parameters with quotes. Defaults to False.

    Returns:
        str: Query with the values changed.
    """

    if replace_parameters is None:
        return query

    separator = '"' if replace_with_quotes else ""

    for replace in range(len(replace_parameters)):
        query = query.replace('`' + str((replace + 1)) + '`', separator + str(replace_parameters[replace]) + separator)
    return query


def sql_in(query=None, values_list=None):
    """
    Transforms a list into an IN statement for SQL queries. This function is deprecated.

    Args:
        query (str, optional): Part of the SQL query.
        values_list (List[Union[str, int, float]], optional): List of values.

    Returns:
        str: Formatted SQL query string.

    Examples
        >>> values_list = [1,2,3,4,5]
        >>> query = 'select * from database where' + sql_in(" col in", values_list)
        >>> "select * from database where col in (1, 2, 3, 4, 5)"
    """

    from warnings import warn
    warn('This is function is deprecated, please use sql_filter instead', DeprecationWarning, stacklevel=2)

    if values_list is None:
        return ""

    if not isinstance(values_list, list):
        values_list = [values_list]
    elif len(values_list) == 0:
        return ""

    return sql_filter(query, values_list)


def sql_filter(query: str = None, values: str | float | int | list[str] | list[float] | list[int] = None) -> str:
    """
    Transforms values into appropriate format for SQL filters.

    Args:
        query (str, optional): Part of the SQL query.
        values (Union[str, float, int, List[str], List[float], List[int]], optional): Values to be inserted in the filter.

    Returns:
        str: Formatted SQL query string.

    Examples:
        >>> values = [1,2,3,4,5]
        >>> query = f'SELECT * FROM database WHERE {sql_filter("col in", values_list)}'
        >>> # output: "SELECT * FROM database WHERE col in (1, 2, 3, 4, 5)"
    """
    if values is None:
        return ""

    formatted_filter_value = _get_formatted_query_filter_value(values)

    if query is None:
        return formatted_filter_value
    else:
        return query + " " + formatted_filter_value


@dispatch((float, int))
def _get_formatted_query_filter_value(filter_value: float | int) -> str:
    return str(filter_value)


@dispatch(str)
def _get_formatted_query_filter_value(filter_value: str) -> str:
    return '"' + filter_value + '"'


@dispatch(list)
def _get_formatted_query_filter_value(filter_value: list[str] | list[float] | list[int]) -> str:
    return str(filter_value).replace('[', '(').replace(']', ')')


def sql_between(query=None, values_list=None):
    """
    Transforms a list into a BETWEEN statement for SQL queries.

    Args:
        query (str, optional): Part of the SQL query.
        values_list (List[Union[str, int, float]], optional): List with start and end values for BETWEEN clause.

    Returns:
        str: Formatted SQL query string.

    Examples
        >>> values_list = ['2018-01-01', '2018-02-02']
        >>> query = f'SELECT * FROM database WHERE {sql_between("date", values_list)}'
        >>> # output: "SELECT * FROM database WHERE date between '2018-01-01' and '2018-02-02'"
    """
    if values_list is None:
        return ""

    if len(values_list) != 2:
        raise Exception("To use sql_between values_list must be of two positions")

    if not isinstance(values_list, list):
        values_list = [values_list]

    if isinstance(values_list[0], int) or isinstance(values_list[1], int):
        between_query = query + " between " + str(values_list[0]) + " and " + str(values_list[1])
    else:
        between_query = query + " between '" + values_list[0] + "' and '" + values_list[1] + "'"

    return between_query


def sql_close(connection: BaseConnection) -> None:
    """
    Function to call a close_connection method, this method was kept for
    retro compatibility matters.
    """
    connection.close_connection()


def add_to_parallel_batch(connection: str | BaseConnection, query, replace_parameters=None, close_connection=True,
                          show_query=False, null_as=None, add_quotes=False, cache_time=None) -> None:
    """

    Function used to create the query parallel request used in `sql_execute_parallel`. This function should be called
    just like a sql_execute, using the same parameters.

    Args:
        connection (str | BaseConnection): Connection name or object
        query (str | dict): sql script to query result set (in Big Query or JDBC database) in a string format.
                            For a MongoDB use in a dict format.
        replace_parameters (list, optional): List of parameters to be used in the query. These parameters will replace the numbers
                                      with `` in the query.
        close_connection (bool, optional): Define if automatically closes the connection. Default is True.
        show_query (bool, optional): Print the query in the console. Default is False.
        null_as (str, optional): Default value to fill null values in the result set. Default is None.
        add_quotes (bool, optional): Involves replaced parameters with quotes. Default is False.
        cache_time (int, optional): Time to leave of cache file in seconds, one might set up to 300 seconds. Default is None.
    
    Examples:
        >>> first_query = "SELECT * FROM table1"
        >>> add_to_parallel_batch("connection_name", first_query)
        >>> 
        >>> second_query = "SELECT * FROM table2"
        >>> add_to_parallel_batch("connection_name", second_query)
    """
    # TODO convert list to dict and impklment UID
    # TODO implment map method
    current_query = {
        "connection": connection,
        "query": query,
        "replace_parameters": replace_parameters,
        "close_connection": close_connection,
        "show_query": show_query,
        "null_as": null_as,
        "add_quotes": add_quotes,
        "cache_time": cache_time
    }

    query_parallel_batch.append(current_query)


def sql_execute_parallel(sql_list=None, number_of_threads=None):
    """
    Function parallelize several queries executions. The queries results will be
    transformed into a list of ObjTable to be used inside the response.

    Args:
        sql_list (list, optional): List of queries to be executed. Default is None.
        number_of_threads (int, optional): Number of threads that going to be used. Default is None.
    
    returns:
        tuple: Tuple with the result of the queries.
    
    Examples:
        >>> first_query = "SELECT * FROM table1"
        >>> add_to_parallel_batch("connection_name", first_query)
        >>> 
        >>> second_query = "SELECT * FROM table2"
        >>> add_to_parallel_batch("connection_name", second_query)
        >>>
        >>> data1, data2 = sql_execute_parallel(number_of_threads=2)
    """

    sql_list = _get_sql_list(sql_list)

    number_of_threads = len(sql_list) if number_of_threads is None else number_of_threads
    query_manager = SqlThreadManager()
    batch_results = query_manager.parallel_execute(sql_list, number_of_threads=number_of_threads)
    query_parallel_batch.clear()

    return batch_results


def _get_sql_list(sql_list):
    if sql_list is None:
        return query_parallel_batch
    else:
        return sql_list


def reload_database_connection(conn_file_path=GlobalCalling.looq.connection_file):
    if os.path.isfile(conn_file_path):
        with open(conn_file_path, "r") as connection_file:
            GlobalCalling.looq.connection_config = json.load(connection_file)
            connection_file.close()
    else:
        print("Missing connection file: " + GlobalCalling.looq.connection_file)
        GlobalCalling.looq.connection_config = None
