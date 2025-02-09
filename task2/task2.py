from trie import Trie


class LongestCommonWord(Trie):

    def find_longest_common_word(self, strings) -> str:
        if not isinstance(strings, list) or not all(isinstance(s, str) for s in strings):
            raise TypeError("Input must be a list of strings")
        if not strings:
            return ""

        for word in strings:
            self.put(word)

        prefix = []
        current = self.root

        while current:
            if len(current.children) == 1 and current.value is None:
                char, next_node = next(iter(current.children.items()))
                prefix.append(char)
                current = next_node
            else:
                break

        return "".join(prefix)