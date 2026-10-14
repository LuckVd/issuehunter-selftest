import unittest
from mathx import clamp


class TestClamp(unittest.TestCase):
    def test_inside(self):
        self.assertEqual(clamp(3, 1, 5), 3)

    def test_below_low(self):
        # documented contract: result within [lo, hi]
        self.assertEqual(clamp(0, 1, 5), 1)

    def test_above_high(self):
        self.assertEqual(clamp(9, 1, 5), 5)


if __name__ == "__main__":
    unittest.main()
