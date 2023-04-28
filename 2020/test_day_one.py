import unittest
from day01.part_one import parse_input, find_sum


class TestPartOne(unittest.TestCase):
    """Test part one module"""

    def setUp(self) -> None:
        """Set up test fixtures"""
        self.values = [1721, 979, 366, 299, 675, 1456]
        self.target = 2020
        self.result = 514579

    def test_parse_no_input(self):
        """Test parse_input with no input file"""
        self.assertRaises(FileNotFoundError, parse_input, 'no_input.txt')

    def test_parse_input(self):
        """Test parse_input with our input file"""
        values = parse_input('input.txt')
        self.assertEqual(len(values), 200)

    def test_find_sum(self):
        """Test find_sum with our values and target"""
        self.assertEqual(find_sum(self.values, self.target), self.result)


if __name__ == '__main__':
    unittest.main()
