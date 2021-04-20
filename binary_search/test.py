import unittest
from binary_search import binary_search


class BinarySearchTestCase(unittest.TestCase):
    def setUp(self):
        self.arr1 = [1, 3, 6, 16, 23, 46]

    def test_binary_search(self):
        self.assertEqual(binary_search(self.arr1, 23), 4)
        self.assertEqual(binary_search(self.arr1, 44), None)
        


if __name__ == '__main__':
    unittest.main()
