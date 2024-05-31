#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#

# @lc code=start
class Node:

    def __init__(self):
        self.is_end = False
        self.children = dict()

class WordDictionary:

    def __init__(self):
        self.word_dict = Node()

    def addWord(self, word: str) -> None:
        node = self.word_dict
        for s in word:
            if s not in node.children:
                node.children[s] = Node()
            node = node.children[s]
        node.is_end = True

    def search(self, word: str) -> bool:

        def traverse(node: Node, index: int) -> bool:
            if index == len(word):
                return node.is_end

            s = word[index]
            if s == '.':
                for child in node.children.values():
                    if traverse(child, index + 1):
                        return True
            if s not in node.children:
                return False
            return traverse(node.children[s], index + 1)

        return traverse(self.word_dict, 0)
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end
