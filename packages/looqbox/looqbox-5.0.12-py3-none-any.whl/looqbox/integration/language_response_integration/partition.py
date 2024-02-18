from multimethod import multimethod

from looqbox.integration.language_response_integration.language_parser import LanguageParser
from looqbox.objects.response_parameters.group_by.group_by import GroupBy
from looqbox.utils.utils import as_dict_ignore_nones


def  extract_partition_values(grouping, only_value, as_dict, default=None):
    """Auxiliary function to extract values from a partition."""
    if only_value:
        return grouping.values if grouping is not None and isinstance(grouping, GroupBy) else default
    if as_dict:
        return [as_dict_ignore_nones(grouping.to_token())] if grouping and isinstance(grouping, GroupBy) else None
    return grouping


@multimethod
def get_partition(partition: str, par_json, partition_default=None, only_value=False, as_dict=True) -> GroupBy:
    """
    Function to search for a specific partition inside the JSON sent by the parser

    :param partition: partition to be found
    :param par_json: JSON from parser
    :param partition_default: Default value to be returned
    :param only_value: if True will only return the partition value
    :return: A Map structure or a single value
    """
    language_parser = LanguageParser()
    if partition == "$date":
        partition = "$datetime"
    grouping = language_parser.get_partitions_filter(partition, partition_default)
    return extract_partition_values(grouping, only_value, as_dict, partition_default)


@multimethod
def get_partition(partitions: list, par_json, partition_default=None, only_value=False, as_dict=True):
    """
    Overloaded function to handle multiple partitions.
    """
    return [get_partition(partition, par_json, partition_default, only_value, as_dict) for partition in partitions]
