from multimethod import multimethod

from looqbox.integration.language_response_integration.language_parser import LanguageParser
from looqbox.objects.response_parameters.condition.condition import Condition
from looqbox.objects.response_parameters.condition.temporal_relation import TemporalRelation
from looqbox.utils.utils import as_dict_ignore_nones


def extract_entity_values(entity, only_value, as_token, as_dict, entity_default, should_evaluate_date_boundaries):
    """Auxiliary function to extract values from an entity."""
    if only_value:
        if isinstance(entity, TemporalRelation):
            if should_evaluate_date_boundaries:
                return [entity.date_with_evaluated_boundaries] if entity is not entity_default else entity_default
        return entity.values if entity is not entity_default else entity_default
    if as_token:
        return entity.to_token(should_evaluate_date_boundaries)
    if as_dict:
        if isinstance(entity, TemporalRelation):
            return [as_dict_ignore_nones(entity.to_token(should_evaluate_date_boundaries))] if entity else None
        return [as_dict_ignore_nones(entity.to_token())] if entity else None
    return entity


@multimethod
def get_entity(entity_tag: str, par_json, entity_default=None, only_value=False,
               should_evaluate_date_boundaries=False, as_dict=True, as_token=False):
    """
    Search for a specific entity inside the JSON provided by the parser.

    :param entity_tag: Entity tag to be found.
    :param par_json: JSON from parser.
    :param entity_default: Default value to be returned if entity is not found.
    :param only_value: If True, only the entity value is returned.
    :param should_evaluate_date_boundaries: If True, reevaluate date boundaries based on the NLP object.
    :param as_token: Return the entity as a token dataclass object (value, segment, text).
    :param as_dict: Return the entity in a dictionary format.
    :return: Either a Map structure or a single value, depending on the parameters.
    """
    language_parser = LanguageParser()

    if entity_tag == "$date":
        entity = _get_datetime_entity_as_date(language_parser, entity_default)
    elif entity_tag == "$comparative":
        return language_parser.get_comparative_nodes(only_value, as_token, as_dict)
    else:
        entity = language_parser.get_entity_filter(entity_tag, entity_default)

    return extract_entity_values(entity, only_value, as_token, as_dict, entity_default, should_evaluate_date_boundaries)


def _get_datetime_entity_as_date(language_parser, entity_default):
    """
    Convert a datetime entity to a date entity.

    :param language_parser: The LanguageParser instance.
    :param entity_default: Default value for the entity.
    :return: Modified entity with parameter_name set to "$date".
    """
    entity = language_parser.get_entity_filter("$datetime", entity_default)
    if entity is not None and isinstance(entity, Condition):
            entity.parameter_name = "$date"
    return entity


@multimethod
def get_entity(entity_tags: list, par_json, entity_default=None, only_value=False,
               should_evaluate_date_boundaries=False, as_dict=True, as_token=False):
    """
    Overloaded function to handle multiple entity tags.
    """
    return [get_entity(tag, par_json, entity_default, only_value,
                       should_evaluate_date_boundaries, as_dict, as_token)
            for tag in entity_tags]
