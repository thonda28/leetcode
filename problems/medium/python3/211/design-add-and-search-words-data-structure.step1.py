#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#

# @lc code=start
class Trie:

    def __init__(self):
        self.is_word = False
        self.children = dict()

class WordDictionary:

    def __init__(self):
        self.word_dictionary = Trie()

    def addWord(self, word: str) -> None:
        trie = self.word_dictionary
        while word:
            if word[0] not in trie.children:
                trie.children[word[0]] = Trie()
            trie = trie.children[word[0]]
            word = word[1:]
        trie.is_word = True

    def search(self, word: str) -> bool:

        def is_word(trie: Trie, word: str) -> bool:
            if not word:
                return trie.is_word
            if word[0] == '.':
                for child in trie.children.values():
                    if is_word(child, word[1:]):
                        return True
            if word[0] not in trie.children:
                return False
            return is_word(trie.children[word[0]], word[1:])

        trie = self.word_dictionary
        return is_word(trie, word)
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end
