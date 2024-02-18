import unittest

from looqbox.utils.dot_notation import Functional


class TestFunctional(unittest.TestCase):
    def test_map(self):
        f = Functional([1, 2, 3])
        result = f.map(lambda x: x * 2).to_list()
        self.assertEqual([2, 4, 6], result)

    def test_map_nested(self):
        f = Functional([[1, 2], [3, 4]])
        result = f.map_nested(lambda x: x * 2).to_list()
        self.assertEqual([[2, 4], [6, 8]], result)

    def test_map_nested_not_none_to_list(self):
        f = Functional([[1, None], [3, 4]])
        result = f.map_nested_not_none_to_list(lambda x: x * 2)
        self.assertEqual([[2], [6, 8]], result)

    def test_filter(self):
        f = Functional([1, 2, 3, 4])
        result = f.filter(lambda x: x % 2 == 0).to_list()
        self.assertEqual([2, 4], result)

    def test_group_by(self):
        f = Functional(['apple', 'banana', 'cherry', 'mango', 'apricot', 'blueberry'])
        result = f.group_by(lambda x: x[0]).to_list()  # grouping by the first letter
        # sorting result for a consistent assertion
        result.sort(key=lambda x: x[0])
        expected = [
            ('a', ['apple', 'apricot']),
            ('b', ['banana', 'blueberry']),
            ('c', ['cherry']),
            ('m', ['mango'])
        ]
        self.assertEqual(expected, result)

    def test_flatten(self):
        f = Functional([[1, 2], [3, 4]])
        result = f.flatten().to_list()
        self.assertEqual([1, 2, 3, 4], result)

    def test_reduce(self):
        f = Functional([1, 2, 3, 4, 5])
        result = f.fold(lambda x, y: x + y)
        self.assertEqual(result, 15)

    def test_product(self):
        f = Functional([1, 2])
        result = f.product([3, 4]).to_list()
        self.assertEqual([(1, 3), (1, 4), (2, 3), (2, 4)], result)

    def test_to_dict(self):
        f = Functional([('one', 1), ('two', 2)])
        result = f.to_dict()
        self.assertEqual({'one': 1, 'two': 2}, result)

    def test_also(self):
        f = Functional([1, 2, 3])
        result = []
        f.also(result.append)
        self.assertEqual([1, 2, 3], result)

    def test_map_dict(self):
        f = Functional({'one': 1, 'two': 2, 'three': 3})
        result = f.map(lambda key, value: f"{key}: {value}").to_list()
        self.assertEqual(["one: 1", "two: 2", "three: 3"], result)

    def test_filter_dict(self):
        f = Functional({'one': 1, 'two': 2, 'three': 3, 'four': 4})
        result = f.filter(lambda key, value: value % 2 == 0).to_dict()
        self.assertEqual({'two': 2, 'four': 4}, result)

    def test_filter_dict_none(self):
        f = Functional({'one': None, 'two': 2, 'three': None, 'four': 4})
        result = f.filter(lambda key, value: value is not None).to_dict()
        self.assertEqual({'two': 2, 'four': 4}, result)

    def test_first(self):
        f = Functional([1, 2, 3, 4])
        result = f.first()
        self.assertEqual(result, 1)

        f = Functional([])
        self.assertIsNone(f.first())

    def test_first_not_none(self):
        f = Functional([None, None, 1, 2, 3, 4])
        result = f.first_not_none()
        self.assertEqual(result, 1)

        f = Functional([None, None])
        self.assertIsNone(f.first_not_none())

    def test_last(self):
        f = Functional([1, 2, 3, 4])
        result = f.last()
        self.assertEqual(result, 4)

        f = Functional([])
        self.assertIsNone(f.last())

    def test_last_not_none(self):
        f = Functional([1, 2, 3, None, None])
        result = f.last_not_none()
        self.assertEqual(result, 3)

        f = Functional([None, None])
        self.assertIsNone(f.last_not_none())

    def test_drop_duplicates(self):
        f = Functional([1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 6, 6])
        result = f.drop_duplicates().to_list()
        self.assertEqual([1, 2, 3, 4, 5, 6], result)

    def test_fold(self):
        f = Functional([1, 2, 3, 4])
        result = f.fold(lambda x, y: x + y, initial=10)
        self.assertEqual(result, 20)

    def test_filter_not_none(self):
        f = Functional([None, 1, None, 2, 3, None])
        result = f.filter_not_none().to_list()
        self.assertEqual([1, 2, 3], result)

    def test_concat(self):
        f1 = Functional([1, 2, 3])
        f2 = Functional([4, 5, 6])
        result = f1.concat(f2.iterable).to_list()
        self.assertEqual([1, 2, 3, 4, 5, 6], result)

    def test_sort_by(self):
        f = Functional([1, 3, 2])
        result = f.sort_by(lambda x: x).to_list()
        self.assertEqual([1, 2, 3], result)

    def test_sort_by_descending(self):
        f = Functional([1, 3, 2])
        result = f.sort_by(lambda x: x, True).to_list()
        self.assertEqual([3, 2, 1], result)

    def test_first_with_lambda(self):
        f = Functional([1, 2, 3, 4])
        result = f.first(lambda x: x % 2 == 0)
        self.assertEqual(result, 2)

    def test_map_not_none(self):
        f = Functional([1, None, 2])
        result = f.map_not_none(lambda x: x * 2).to_list()
        self.assertEqual([2, 4], result)

    def test_flat_map(self):
        f = Functional([1, 2])
        result = f.flat_map(lambda x: [x, x * 2]).to_list()
        self.assertEqual([1, 2, 2, 4], result)

    def test_flat_map_not_none(self):
        f = Functional([1, None, 2])
        result = f.flat_map_not_none(lambda x: [x, x * 2] if x else None).to_list()
        self.assertEqual([1, 2, 2, 4], result)

    def test_associate(self):
        f = Functional([1, 2, 3])
        result = f.associate(lambda it: (it * 3, it * 2))
        self.assertEqual({3: 2, 6: 4, 9: 6}, result)

    def test_associate_by(self):
        f = Functional([1, 2, 3])
        result = f.associate_by(lambda it: it * 2)
        self.assertEqual({2: 1, 4: 2, 6: 3}, result)

    def test_associate_by_not_none(self):
        f = Functional([1, 2, 3, None])
        result = f.associate_by_not_none(lambda it: it * 2)
        self.assertEqual({2: 1, 4: 2, 6: 3}, result)

    def test_associate_with(self):
        f = Functional([1, 2, 3])
        result = f.associate_with(lambda it: it * 2)
        self.assertEqual({1: 2, 2: 4, 3: 6}, result)

    def test_associate_with_not_none(self):
        f = Functional([1, 2, 3, None])
        result = f.associate_with_not_none(lambda it: it * 2)
        self.assertEqual({1: 2, 2: 4, 3: 6}, result)

    def test_filter_indexed_with_empty_iterable(self):
        f = Functional([])
        result = f.filter_indexed(lambda i, x: x > 0).to_list()
        self.assertEqual(result, [])

    def test_to_list_with_nested_iterable(self):
        f = Functional([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
        result = f.to_list()
        self.assertEqual([[[1, 2], [3, 4]], [[5, 6], [7, 8]]], result)

    def test_fold_indexed_with_lambda_multiplying_indices(self):
        f = Functional([1, 2, 3, 4, 5])
        result = f.fold_indexed(lambda i, acc, x: acc * x)
        self.assertEqual(result, 120)

    def test_also_with_lambda_appending_to_result_list(self):
        f = Functional([1, 2, 3])
        result = []
        f.also(result.append)
        self.assertEqual([1, 2, 3], result)

    def test_map_with_empty_iterable(self):
        f = Functional([])
        result = f.map(lambda x: x * 2).to_list()
        self.assertEqual(result, [])

    def test_concat_with_non_empty_iterables(self):
        f1 = Functional([1, 2, 3])
        f2 = Functional([4, 5, 6])
        result = f1.concat(f2.iterable).to_list()
        self.assertEqual([1, 2, 3, 4, 5, 6], result)

    def test_fold_indexed_with_empty_iterable(self):
        f = Functional([])
        result = f.fold_indexed(lambda i, acc, x: acc + i)
        self.assertEqual(result, None)

    def test_associate_with_with_none_values(self):
        f = Functional([1, 2, 3])
        result = f.associate_with(lambda it: it * 2)
        self.assertEqual({1: 2, 2: 4, 3: 6}, result)

    def test_flatten_to_list_with_deeply_nested_iterable(self):
        f = Functional([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
        result = f.flatten_to_list()
        self.assertEqual([[1, 2], [3, 4], [5, 6], [7, 8]], result)

    def test_last_indexed_not_none_to_list_with_empty_iterable(self):
        f = Functional([])
        result = f.last_indexed_not_none_to_list(lambda i, x: x if i % 2 != 0 else None)
        self.assertEqual(result, [])

    def test_fold_not_none_to_set_with_lambda_summing_values(self):
        f = Functional([1, 2, 3, None, 4, None])
        result = f.fold_not_none_to_set(lambda acc, x: acc + x, initial=0)
        self.assertEqual(result, {10})

    def test_group_by_with_strings_length(self):
        f = Functional(['apple', 'banana', 'cherry', 'mango', 'apricot', 'blueberry'])
        result = f.group_by(lambda x: len(x)).to_list()
        result.sort(key=lambda x: x[0])
        expected = [(5, ['apple', 'mango']),
                    (6, ['banana', 'cherry']),
                    (7, ['apricot']),
                    (9, ['blueberry'])]
        self.assertEqual(expected, result)

    def test_flatten_to_set_with_empty_iterable(self):
        f = Functional([])
        result = f.flatten_to_set()
        self.assertEqual({}, result)

    def test_map_not_none_with_empty_iterable(self):
        f = Functional([])
        result = f.map_not_none(lambda x: x * 2).to_list()
        self.assertEqual(result, [])

    def test_filter_to_set_with_lambda_filtering_odd_numbers(self):
        f = Functional([1, 2, 3, 4, 5])
        result = f.filter(lambda x: x % 2 == 0).to_set()
        self.assertEqual({2, 4}, result)

    def test_map_not_none_with_none_values(self):
        f = Functional([1, None, 2])
        result = f.map_not_none(lambda x: x * 2).to_list()
        self.assertEqual([2, 4], result)

    def test_fold_indexed_with_lambda_summing_indices(self):
        f = Functional([1, 2, 3, 4, 5])
        result = f.fold_indexed(lambda i, acc, x: acc + i)
        self.assertEqual(11, result)

    def test_last_indexed_not_none_to_set_with_none_values(self):
        f = Functional([1, None, 2, None, 3, None])
        result = f.last_indexed_not_none_to_set(lambda i, x: x if i % 2 != 0 else None)
        self.assertEqual({}, result)

    def test_flatten_to_set_with_nested_list_duplicates(self):
        f = Functional([[1, 2], [2, 3], [3, 4]])
        result = f.flatten_to_set()
        self.assertEqual({1, 2, 3, 4}, result)

    def test_fold_with_lambda_multiplying_values(self):
        f = Functional([1, 2, 3, 4, 5])
        result = f.fold_indexed(lambda i, acc, x: acc * x)
        self.assertEqual(result, 120)

    def test_filter_indexed_not_none_to_list_with_list_containing_None_and_lambda_filtering_odd_indices(self):
        f = Functional([1, None, 2, None, 3, None])
        result = f.filter_indexed_not_none_to_list(lambda i, x: x is not None and i % 2 != 0)
        self.assertEqual([], result)

    def test_fold_indexed_with_lambda_summing_index_and_value(self):
        f = Functional([1, 2, 3, 4, 5])
        result = f.fold_indexed(lambda i, acc, x: acc + i + x)
        self.assertEqual(25, result)

    def test_last_indexed_to_set_with_empty_iterable(self):
        f = Functional([])
        result = f.last_indexed_to_set(lambda i, x: x if i % 2 != 0 else None)
        self.assertEqual(result, set())

    def test_associate_by_with_none_values(self):
        f = Functional([1, 2, 3])
        result = f.associate_by(lambda it: it * 2)
        self.assertEqual({2: 1, 4: 2, 6: 3}, result)

    def test_fold_with_empty_iterable(self):
        f = Functional([])
        result = f.fold(lambda x, y: x + y, initial=10)
        self.assertEqual(result, 10)

    def test_associate_with_concatenation(self):
        f = Functional([(1, 'a'), (2, 'b'), (3, 'c')])
        result = f.associate(lambda it: (it[0], it[1] + it[1]))
        self.assertEqual({1: 'aa', 2: 'bb', 3: 'cc'}, result)
