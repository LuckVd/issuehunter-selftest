import unittest
from stats import average


class TestAverage(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(average([1, 2, 3]), 2.0)

    def test_empty_returns_zero(self):
        # documented contract
        self.assertEqual(average([]), 0.0)


if __name__ == "__main__":
    unittest.main()
