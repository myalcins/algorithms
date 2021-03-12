import unittest
from insertion_sort import insertion_sort


class TestInsertionSort(unittest.TestCase):
    def setUp(self):
        self.arr1 = [5, 2, 4, 6, 1, 3]
        self.arr2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    def test_insertion_sort(self):
        self.assertEqual(insertion_sort(self.arr1), sorted(self.arr1))
        self.assertEqual(insertion_sort(self.arr2), sorted(self.arr2))


if __name__ == '__main__':
    unittest.main()
