import unittest

max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_in_middle(self):
        self.assertEqual(max_integer([1, 4, 2, 3]), 4)

    def test_one_negative_number(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

    def test_single_element(self):
        self.assertEqual(max_integer([4]), 4)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_all_same_elements(self):
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)

    def test_floats(self):
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4.4]), 4.4)

    def test_mixed_ints_and_floats(self):
        self.assertEqual(max_integer([1, 2.2, 3, 4.4]), 4.4)

if __name__ == '__main__':
    unittest.main()