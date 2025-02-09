import unittest

from task2 import LongestCommonWord


class TestLongestCommonWord(unittest.TestCase):
    def setUp(self):
        self.trie = LongestCommonWord()

    def test_find_longest_common_word(self):
        test_cases = [
            (["flower", "flow", "flight"], "fl"),
            (["interspecies", "interstellar", "interstate"], "inters"),
            (["dog", "racecar", "car"], ""),
            (["throne", "throne"], "throne"),
            ([""], ""),
            ([], ""),
        ]
        for strings, expected in test_cases:
            with self.subTest(strings=strings):
                self.trie = LongestCommonWord()
                if all(strings):
                    self.assertEqual(self.trie.find_longest_common_word(strings), expected)
                else:
                    self.assertEqual(expected, "")


if __name__ == "__main__":
    unittest.main()