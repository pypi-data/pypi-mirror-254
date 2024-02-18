import datetime
from datetime import timedelta

from multimethod import multimethod

from looqbox.config.logger import Logger
from looqbox.global_calling import GlobalCalling
from looqbox.objects.response_parameters.condition.comparative.comparison_node import ComparisonNode
from looqbox.objects.response_parameters.condition.condition import Condition
from looqbox.objects.response_parameters.group_by.group_by import GroupBy
from looqbox.objects.response_parameters.keyword.keyword import Keyword
from looqbox.utils.dot_notation import Functional
from looqbox.utils.utils import as_dict_ignore_nones


class LanguageParser:
    """
    Interface to parse and to retrieve parameteres from Looqbox's NPl object

    This class aim to serve as a middle-ground for the user and the NLP objects, hence providing methods and tools
    to search and to get entities, partitions and keywords (to name a few) from a more complex object.

    Attributes:
    language_content (dict): Looqbox's Language (NLP) object.

    Examples:
    >>> language_content = LanguageParser(par)
    >>> entity = language_content.get_entity_filter("$date",
    ...                                             entity_default=[["2023-01-01", 2023-12-31]])
    """

    def __init__(self):

        self.response_filters = GlobalCalling.looq.response_filters or dict()
        self.response_keywords = GlobalCalling.looq.response_keywords or dict()
        self.response_groupings = GlobalCalling.looq.response_partitions or dict()
        self.response_parameters = GlobalCalling.looq.response_parameters or dict()
        self.syntax_tree = GlobalCalling.looq.syntax_tree or None
        self.logger = Logger.get_logger(__name__)

    def get_entity_filter(self, entity_name: str, default_value: any = None) -> Condition:

        """
        Method to get an entity value from Looqbox's NPL object.
        
        Args:
        entity_name (str): The entity name, usually beginning with the "$" symbol
        default_value (dict|list[list[any]], optional): The value that will be used if the NPL does not contain
         the entity searched for, usually, this value will be a list or a None value, .e.g [[1, 2]].
        
        Returns: 
        Entity: This method returns the asked entity properties and its values in form of an Entity class instance
        
        Example:
        to get a state from the NLP parser:
       >>> asked_state = LanguageParser.get_entity_filter("$state", entity_default_value = [["NY", "CA"]])
        """
        return self.response_filters.get(entity_name, default_value)

    def get_partitions_filter(self, partition_name, default_value=None) -> GroupBy:

        """
        Method to get a partiton value from Looqbox's NPL object.

        Args:
        partition_name (str): The partition name, usually beginning with the "$" symbol
        partition_default_value (dict|list[str], optional): The value that will be used if the NPL does not contain the
         partition searched for, usually, this value will be a list or a None value, .e.g ["by day"].

        Returns:
        Grouping: This method returns the asked partition properties and its values in form of a Grouping class instance

        Example:
        to get a state from the NLP parser:
        >>> date_aggregation = LanguageParser.get_partitions_filter("date", entity_default_value = ["by week"])
        """

        return self.response_groupings.get(partition_name, default_value)

    def get_asked_keywords(self, keyword_name, default_value=None) -> Keyword:

        """
        Method to get a keyword value from Looqbox's NPL object.

        Args:
        keyword_name (str): The keyword name
        keyword_default_value (dict|list[str], optional): The value that will be used if the NPL does not contain the
         keyword searched for, usually, this value will be a list or a None value, .e.g ["campanha"].

        Returns:
        Keyword: This method returns the asked keyword properties and its values in form of a Keyword class instance

        Example:
        to get a state from the NLP parser:
        >>> keyword_asked = LanguageParser.get_asked_keywords("loja", keyword_default_value = ["estabelecimento"])
        """

        return self.response_keywords.get(keyword_name, default_value)

    def get_comparative_nodes(self, only_value=False, as_token=False, as_dict=True):
        if not self.syntax_tree:
            self.logger.error("No syntax tree found")
            return None
        nodes = self.syntax_tree.recursively_get_self_and_children_nodes()
        comparative_nodes = Functional(nodes).filter_not_none_to_list(lambda it: isinstance(it, ComparisonNode))
        tokens = Functional(comparative_nodes).map_not_none_to_list(lambda it: it.to_token())
        if not comparative_nodes:
            return None
        if only_value:
            return Functional(comparative_nodes).map_not_none_to_list(lambda it: it.values)
        if as_token:
            return tokens
        if as_dict:
            return (
                Functional(tokens)
                .map_not_none(lambda it: as_dict_ignore_nones(it)).to_list()
            )
        return comparative_nodes
