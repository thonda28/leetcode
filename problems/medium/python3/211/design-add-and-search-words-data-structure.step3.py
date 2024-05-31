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
        self.word_dict = Trie()

    def addWord(self, word: str) -> None:
        trie = self.word_dict
        for s in word:
            if s not in trie.children:
                trie.children[s] = Trie()
            trie = trie.children[s]
        trie.is_word = True

    def search(self, word: str) -> bool:

        def _is_word(trie: Trie, index: int) -> bool:
            if index == len(word):
                return trie.is_word

            s = word[index]
            if s == '.':
                for child in trie.children.values():
                    if _is_word(child, index + 1):
                        return True
            if s not in trie.children:
                return False
            return _is_word(trie.children[s], index + 1)

        return _is_word(self.word_dict, 0)
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end
