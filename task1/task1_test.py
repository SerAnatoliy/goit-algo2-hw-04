import unittest

from task1 import Homework


class TestHomework(unittest.TestCase):
    def setUp(self):
        self.trie = Homework()
        words = ["apple", "application", "banana", "cat"]
        for i, word in enumerate(words):
            self.trie.put(word, i)

    def test_count_words_with_suffix(self):
        test_cases = [
            ("e", 1),    # apple
            ("ion", 1),  # application
            ("a", 1),    # banana
            ("at", 1),   # cat
            ("z", 0)     # no matches
        ]
        for pattern, expected in test_cases:
            with self.subTest(pattern=pattern):
                self.assertEqual(self.trie.count_words_with_suffix(pattern), expected)

    def test_has_prefix(self):
        test_cases = [
            ("app", True),  # apple, application
            ("bat", False), # no matches
            ("ban", True),  # banana
            ("ca", True),   # cat
            ("dog", False)  # no matches
        ]
        for prefix, expected in test_cases:
            with self.subTest(prefix=prefix):
                self.assertEqual(self.trie.has_prefix(prefix), expected)


if __name__ == "__main__":
    unittest.main()