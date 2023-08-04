# TrieBased_AutocompleteApp/trie.py
from .models import Word

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

    def add_word(self, word):
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def get_words(self, prefix=""):
        words = []
        if self.is_end_of_word:
            words.append(prefix)

        for char, child_node in self.children.items():
            words.extend(child_node.get_words(prefix + char))

        return words


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        self.root.add_word(word)

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def autocomplete(self, prefix, num_suggestions=5):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]

        suggestions = []
        self._find_suggestions(node, prefix, num_suggestions, suggestions)
        return suggestions

    def _find_suggestions(self, node, current_word, num_suggestions, suggestions):
        if len(suggestions) >= num_suggestions:
            return

        if node.is_end_of_word:
            suggestions.append(current_word)

        for char, child_node in node.children.items():
            self._find_suggestions(child_node, current_word + char, num_suggestions, suggestions)

    def get_words(self):
        return self.root.get_words()


def populate_trie(trie, filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            word = line.strip()
            if word:
                trie.insert(word)
