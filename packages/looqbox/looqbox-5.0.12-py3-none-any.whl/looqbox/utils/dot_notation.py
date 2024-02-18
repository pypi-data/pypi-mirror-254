import functools
import itertools
from itertools import chain
from typing import Union


class Functional:
    def __init__(self, iterable=None):
        self.iterable = iterable or list()

    def map(self, func):
        if self._is_dict():
            return Functional(map(lambda item: func(*item), self.iterable.items()))
        return Functional(map(func, self.iterable))

    def map_to_list(self, function):
        return self.map(function).to_list()

    def map_to_set(self, function):
        return self.map(function).to_set()

    def map_not_none(self, function):
        return self.filter_not_none().map(function).filter_not_none()

    def map_not_none_to_list(self, function):
        return self.map_not_none(function).to_list()

    def map_not_none_to_set(self, function):
        return self.map_not_none(function).to_set()

    def map_indexed(self, function):
        if self._is_dict():
            return Functional({k: function(i, k, v) for i, (k, v) in enumerate(self.iterable.items())})
        return Functional([function(i, x) for i, x in enumerate(self.iterable)])

    def map_indexed_to_list(self, function):
        return self.map_indexed(function).to_list()

    def map_indexed_to_set(self, function):
        return self.map_indexed(function).to_set()

    def map_indexed_not_none(self, function):
        return self.filter_not_none().map_indexed(function).filter_not_none()

    def map_indexed_not_none_to_list(self, function):
        return self.map_indexed_not_none(function).to_list()

    def map_indexed_not_none_to_set(self, function):
        return self.map_indexed_not_none(function).to_set()

    def map_nested(self, function):
        if self._is_dict():
            return Functional([Functional(v).map(function) for k, v in self.iterable.items()])
        return self.map(lambda it: Functional(it).map(function))

    def map_nested_to_list(self, function):
        return self.map_nested(function).to_list()

    def map_nested_to_set(self, function):
        return self.map_nested(function).to_set()

    def map_nested_not_none(self, function):
        return self.map_not_none(lambda it: Functional(it).map_not_none_to_list(function))

    def map_nested_not_none_to_list(self, function):
        return self.map_nested_not_none(function).to_list()

    def map_nested_not_none_to_set(self, function):
        return self.map_nested_not_none(function).to_set()

    def map_nested_indexed(self, function):
        if self._is_dict():
            return Functional([Functional(v).map_indexed_to_list(function) for k, v in self.iterable.items()])
        return Functional(self.map(lambda it: Functional(it).map_indexed_to_list(function)))

    def map_nested_indexed_to_list(self, function):
        return self.map_nested_indexed(function).to_list()

    def map_nested_indexed_to_set(self, function):
        return self.map_nested_indexed(function).to_set()

    def map_nested_indexed_not_none(self, function):
        return self.map_not_none(lambda it: Functional(it).map_indexed_not_none(function))

    def map_nested_indexed_not_none_to_list(self, function):
        return self.map_nested_indexed_not_none(function).to_list()

    def map_nested_indexed_not_none_to_set(self, function):
        return self.map_nested_indexed_not_none(function).to_set()

    def flat_map(self, function):
        return self.map(function).flatten()

    def flat_map_to_list(self, function):
        return self.flat_map(function).to_list()

    def flat_map_to_set(self, function):
        return self.flat_map(function).to_set()

    def flat_map_not_none(self, function):
        return self.map_not_none(function).flatten()

    def flat_map_not_none_to_list(self, function):
        return self.flat_map_not_none(function).to_list()

    def flat_map_not_none_to_set(self, function):
        return self.flat_map_not_none(function).to_set()

    def flat_map_nested(self, function):
        return self.map_nested(function).flatten()

    def flat_map_nested_to_list(self, function):
        return self.flat_map_nested(function).to_list()

    def flat_map_nested_to_set(self, function):
        return self.flat_map_nested(function).to_set()

    def flat_map_nested_not_none(self, function):
        return self.map_nested_not_none(function).flatten()

    def flat_map_nested_not_none_to_list(self, function):
        return self.flat_map_nested_not_none(function).to_list()

    def flat_map_nested_not_none_to_set(self, function):
        return self.flat_map_nested_not_none(function).to_set()

    def flat_map_nested_indexed(self, function):
        return self.map_nested_indexed(function).flatten()

    def flat_map_nested_indexed_to_list(self, function):
        return self.flat_map_nested_indexed(function).to_list()

    def flat_map_nested_indexed_to_set(self, function):
        return self.flat_map_nested_indexed(function).to_set()

    def flat_map_indexed(self, function):
        return self.map_indexed(function).flatten()

    def flat_map_indexed_to_list(self, function):
        return self.flat_map_indexed(function).to_list()

    def flat_map_indexed_to_set(self, function):
        return self.flat_map_indexed(function).to_set()

    def flat_map_indexed_not_none(self, function):
        return self.map_indexed_not_none(function).flatten()

    def flat_map_indexed_not_none_to_list(self, function):
        return self.flat_map_indexed_not_none(function).to_list()

    def flat_map_indexed_not_none_to_set(self, function):
        return self.flat_map_indexed_not_none(function).to_set()

    def filter(self, func):
        if isinstance(self.iterable, dict):
            return Functional(list(filter(lambda item: func(*item), self.iterable.items())))
        else:
            return Functional(list(filter(func, self.iterable)))

    def filter_to_list(self, function):
        return self.filter(function).to_list()

    def filter_to_set(self, function):
        return self.filter(function).to_set()

    def filter_not_none(self, func=None):
        if func is not None:
            return self.filter(lambda it: it is not None and func(it))
        return self.filter(lambda it: it is not None)

    def filter_not_none_to_list(self, function=None):
        return self.filter_not_none(function).to_list()

    def filter_not_none_to_set(self, function=None):
        return self.filter_not_none(function).to_set()

    def filter_indexed(self, function):
        def wrapped(item):
            return function(*item if self._is_dict() else (item[0], item[1]))

        filtered = filter(lambda item: wrapped(item), enumerate(self._dict_or_iterable()))
        return Functional(dict(filtered)) if self._is_dict() else Functional(*filtered)

    def filter_indexed_to_list(self, function):
        return self.filter_indexed(function).to_list()

    def filter_indexed_to_set(self, function):
        return self.filter_indexed(function).to_set()

    def filter_indexed_not_none(self, function=None):
        base_indexes = enumerate(self._dict_or_iterable())
        first_layer_filter = filter(lambda item: item[1] is not None, base_indexes)

        def wrapped(item):
            return function(*item if self._is_dict() else (item[0], item[1]))

        filtered = filter(lambda item: wrapped(item), first_layer_filter)
        functional = Functional(dict(filtered)) if self._is_dict() else Functional(*filtered)

        return functional.filter_not_none()

    def filter_indexed_not_none_to_list(self, function=None):
        return self.filter_indexed_not_none(function).to_list()

    def filter_indexed_not_none_to_set(self, function=None):
        return self.filter_indexed_not_none(function).to_set()

    def first(self, function=None):
        try:
            if function:
                return next(filter(function, self.iterable), None)
            return next(iter(self.iterable), None)
        except StopIteration:
            return None

    def first_to_list(self, function=None):
        return self.first(function).to_list()

    def first_to_set(self, function=None):
        return self.first(function).to_set()

    def first_not_none(self, function=None):
        return self.filter_not_none().first(function)

    def first_not_none_to_list(self, function=None):
        return self.first_not_none(function).to_list()

    def first_not_none_to_set(self, function=None):
        return self.first_not_none(function).to_set()

    def first_indexed(self, function=None):
        try:
            if function:
                return next((x for i, x in enumerate(self.iterable) if function(i, x)), None)
            return self.first()
        except StopIteration:
            return None

    def first_indexed_to_list(self, function=None):
        return self.first_indexed(function).to_list()

    def first_indexed_to_set(self, function=None):
        return self.first_indexed(function).to_set()

    def first_indexed_not_none(self, function=None):
        base_indexes = enumerate(self.iterable)
        first_layer_filter = filter(lambda item: item[1] is not None, base_indexes)

        try:
            if function:
                return next((x for i, x in first_layer_filter if function(i, x)), None)
            return self.first()
        except StopIteration:
            return None

    def first_indexed_not_none_to_list(self, function=None):
        return self.first_indexed_not_none(function).to_list()

    def first_indexed_not_none_to_set(self, function=None):
        return self.first_indexed_not_none(function).to_set()

    def last(self, function=None):
        try:
            if function:
                return next(filter(function, reversed(self.iterable)))
            return next(iter(reversed(self.iterable)))
        except StopIteration:
            return None

    def last_to_list(self, function=None):
        return self.last(function).to_list()

    def last_to_set(self, function=None):
        return self.last(function).to_set()

    def last_not_none(self, function=None):
        return self.filter_not_none().last(function)

    def last_not_none_to_list(self, function=None):
        result = self.last_not_none(function)
        return [result] if result is not None else []

    def last_not_none_to_set(self, function=None):
        result = self.last_not_none(function)
        return {result} if result is not None else set()

    def last_indexed(self, function=None):
        try:
            if function:
                items_with_index = [(i, x) for i, x in enumerate(self.iterable) if function(i, x)]
                return next((x for i, x in reversed(items_with_index)), None)
            return self.last()
        except StopIteration:
            return None

    def last_indexed_to_list(self, function=None):
        result = self.last_indexed(function)
        return [result] if result is not None else []

    def last_indexed_to_set(self, function=None):
        result = self.last_indexed(function)
        return {result} if result is not None else set()

    def last_indexed_not_none(self, function=None):
        base_indexes = enumerate(self.iterable)
        first_layer_filter = list(filter(lambda item: item[1] is not None, base_indexes))

        try:
            if function:
                return next((x for i, x in reversed(first_layer_filter) if function(i, x)), None)
            return self.first()
        except StopIteration:
            return None

    def last_indexed_not_none_to_list(self, function=None):
        result = self.last_indexed_not_none(function)
        return [result] if result is not None else []

    def last_indexed_not_none_to_set(self, function=None):
        result = self.last_indexed_not_none(function)
        return {result} if result is not None else {}

    def fold(self, function, initial=None):
        iterator = iter(self.iterable)
        initial = next(iterator) if initial is None else initial
        return functools.reduce(function, iterator, initial)

    def fold_to_list(self, function, initial=None):
        return [self.fold(function, initial)]

    def fold_to_set(self, function, initial=None):
        result = self.fold(function, initial)
        return {result} if result is not None else set()

    def fold_not_none(self, function, initial=None):
        return self.filter_not_none().fold(function, initial)

    def fold_not_none_to_list(self, function, initial=None):
        return [self.fold_not_none(function, initial)]

    def fold_not_none_to_set(self, function, initial=None):
        result = self.fold_not_none(function, initial)
        return {result} if result is not None else set()

    def fold_indexed(self, function, initial=None):
        iterator = iter(self.iterable)
        initial = next(iterator, None) if initial is None else initial
        zipped = zip(range(1, len(self.iterable)), iterator)

        def wrapper(acc, idx_it):
            idx, it = idx_it
            return function(idx, acc, it)

        return functools.reduce(wrapper, zipped, initial)

    def fold_indexed_to_list(self, function, initial=None):
        return [self.fold_indexed(function, initial)]

    def fold_indexed_to_set(self, function, initial=None):
        result = self.fold_indexed(function, initial)
        return {result} if result is not None else set()

    def fold_indexed_not_none(self, function, initial=None):
        return self.filter_not_none().fold_indexed(function, initial)

    def fold_indexed_not_none_to_list(self, function, initial=None):
        return [self.fold_indexed_not_none(function, initial)]

    def fold_indexed_not_none_to_set(self, function, initial=None):
        result = self.fold_indexed_not_none(function, initial)
        return {result} if result is not None else set()

    def associate(self, transform):
        return {key: value for key, value in self.map(transform).to_list()}

    def associate_by(self, key_selector):
        return {key_selector(item): item for item in self.iterable}

    def associate_by_not_none(self, key_selector):
        return {key_selector(item): item for item in self.iterable if item is not None and key_selector(item) is not None}

    def associate_with(self, value_transform):
        return {item: value_transform(item) for item in self.iterable}

    def associate_with_not_none(self, value_transform):
        return {item: value_transform(item) for item in self.iterable if item is not None and value_transform(item) is not None}

    def also(self, func):
        new_iterable = list()
        for item in self.iterable:
            func(item)
            new_iterable.append(item)
        return Functional(new_iterable)

    def group_by(self, function):
        return Functional((k, list(g)) for k, g in itertools.groupby(sorted(self.iterable, key=function), key=function))

    def drop_duplicates(self):
        return Functional(list(dict.fromkeys(self.iterable)))

    def concat(self, other):
        return Functional(self.iterable + other)

    def sort_by(self, key_func, reverse=False):
        return Functional(sorted(self.iterable, key=key_func, reverse=reverse))

    def product(self, *iterables, repeat=1):
        return Functional(itertools.product(self.iterable, *iterables, repeat=repeat))

    def flatten(self):
        return Functional(chain(*self._to_list(self.iterable)))

    def flatten_to_list(self):
        return self.flatten().to_list()

    def flatten_to_set(self):
        list_ = self.flatten_to_list()
        if not list_:
            return {}
        return set(list_)

    def to_list(self):
        return list(map(self._to_list, self.iterable))

    def to_dict(self, key_function=None):
        if not key_function:
            return dict(self.iterable)
        return {key_function(item): item for item in self.iterable}

    def to_set(self):
        list_ = self.to_list()
        if not list_:
            return {}
        return set(self.to_list())

    def _to_list(self, item):
        if isinstance(item, Functional):
            return self._to_list(item.iterable)
        elif isinstance(item, Union[map, chain, filter, itertools.product]):
            return list(self._to_list(element) for element in item)
        else:
            return item

    def _is_dict(self):
        return isinstance(self.iterable, dict)

    def _dict_or_iterable(self):
        return self.iterable.items() if self._is_dict() else self.iterable

    @staticmethod
    def _verify_func_and_arguments(function, *args):
        return all(args) and function(*args) is not None
