import unittest

from prefixutil import remove_prefix


class PrefixTests(unittest.TestCase):
    def test_removes_one_exact_prefix(self):
        self.assertEqual("abc", remove_prefix("ababc", "ab"))

    def test_nonmatching_prefix_leaves_text_unchanged(self):
        self.assertEqual("bahello", remove_prefix("bahello", "ab"))

    def test_empty_text_remains_empty(self):
        self.assertEqual("", remove_prefix("", "ab"))

    def test_empty_prefix_leaves_text_unchanged(self):
        self.assertEqual("hello", remove_prefix("hello", ""))


if __name__ == "__main__":
    unittest.main()
