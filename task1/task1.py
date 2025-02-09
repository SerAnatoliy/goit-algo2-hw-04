from task2.trie import Trie


class Homework(Trie):
    def count_words_with_suffix(self, pattern) -> int:
        if not isinstance(pattern, str):
            raise TypeError("Pattern must be a string")

        def ends_with(word, suffix):
            return word.endswith(suffix)

        return sum(1 for word in self.keys() if ends_with(word, pattern))

    def has_prefix(self, prefix) -> bool:
        if not isinstance(prefix, str):
            raise TypeError("Prefix must be a string")

        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True