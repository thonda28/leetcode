#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#

# @lc code=start
class WordDictionary:

    def __init__(self):
        self.word_dict = set()

    def addWord(self, word: str) -> None:
        self.word_dict.add(word)

    def search(self, word: str) -> bool:
        num_periods = word.count('.')
        if num_periods == 0:
            return word in self.word_dict
        if num_periods == 1:
            for i in range(26):
                word_replaced_dot = word.replace('.', chr(i + 97))
                if word_replaced_dot in self.word_dict:
                    return True
            return False
        if num_periods == 2:
            for i in range(26):
                word_replaced_one_dot = word.replace('.', chr(i + 97), 1)
                for j in range(26):
                    word_replaced_two_dot = \
                        word_replaced_one_dot.replace('.', chr(j + 97))
                    if word_replaced_two_dot in self.word_dict:
                        return True
            return False
        raise ValueError("The number of period in word must be less than 3")
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end
