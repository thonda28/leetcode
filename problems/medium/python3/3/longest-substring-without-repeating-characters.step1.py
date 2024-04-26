#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        index_map = dict()
        start = -1
        length = 0
        for i, char in enumerate(s):
            if char in index_map:
                start = max(start, index_map[char])
            index_map[char] = i
            length = max(length, i - start)
        return length
# @lc code=end
