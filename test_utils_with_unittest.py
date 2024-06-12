import unittest
from utils import my_sum;

class TestUtils(unittest.TestCase):
    def test_sum_of_two_positives_numbers(self):
        self.assertEqual(my_sum(1,2), 3)
        self.assertEqual(my_sum(2,1), 3)
        self.assertEqual(my_sum(2,2), 4)

    def test_sum_of_neg_and_pos_numbers(self):
        self.assertEqual(my_sum(-1,2), 1)
        self.assertEqual(my_sum(-2,1), -1)
        self.assertEqual(my_sum(2,-2), 0)

    def test_sum_fail_for_string(self):
        with self.assertRaises(Exception):
            my_sum("a", 3)
        with self.assertRaises(Exception):
            my_sum(1, "z")
            


if __name__ == '__main__':
    unittest.main()
