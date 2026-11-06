import unittest

from prefixutil import remove_prefix


class PrefixTests(unittest.TestCase):
    def test_empty_prefix_leaves_text_unchanged(self):
        self.assertEqual("hello", remove_prefix("hello", ""))


if __name__ == "__main__":
    unittest.main()
