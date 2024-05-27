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
        n_period = word.count('.')
        if n_period == 0:
            return word in self.word_dict
        if n_period == 1:
            i_period = word.index('.')
            for i in range(26):
                word_candidate = word[:i_period] + chr(i + 97) + word[i_period + 1:]
                if word_candidate in self.word_dict:
                    return True
            return False
        if n_period == 2:
            i_period1 = word.index('.')
            i_period2 = word.rindex('.')
            for i in range(26):
                for j in range(26):
                    word_candidate = word[:i_period1] + chr(i + 97) + word[i_period1 + 1:i_period2] + chr(j + 97) + word[i_period2 + 1:]
                    if word_candidate in self.word_dict:
                        return True
            return False
        raise ValueError("The number of period in word must be less than 3")
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end
