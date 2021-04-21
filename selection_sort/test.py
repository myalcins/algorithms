import unittest
from selection_sort import selection_sort


class SelectionSortTestCase(unittest.TestCase):
    def setUp(self):
        self.arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]

    def test_selection_sort(self):
        self.assertEqual(selection_sort(self.arr), [1, 2, 3, 4, 5, 6, 7, 8, 9])
        

if __name__ == '__main__':
    unittest.main()