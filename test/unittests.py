import os, sys
import unittest
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from get_pair import PairNumbers


class TestClassPairNumbers(unittest.TestCase):

    def test_get_pairs(self):
        get_pairs_numbers = PairNumbers()
        expected_sum = 10
        CSV_FILE_NAME = 'test/arrayInfoTest'
        self.assertEqual(get_pairs_numbers.get_pairs(expected_sum, CSV_FILE_NAME), {9: 1})


if __name__ == "__main__":
    unittest.main()
