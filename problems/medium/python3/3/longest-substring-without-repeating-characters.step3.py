#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index_map = dict()
        start = 0
        longest_length = 0
        for i, char in enumerate(s):
            if char in char_index_map:
                start = max(start, char_index_map[char] + 1)
            char_index_map[char] = i
            longest_length = max(longest_length, i - start + 1)
        return longest_length
# @lc code=end
