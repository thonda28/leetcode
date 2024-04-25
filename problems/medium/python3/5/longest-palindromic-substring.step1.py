#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        longest_length, longest_palindrome = self.get_palindrome(s, 0, 0)
        for i in range(1, n):
            _length1, _palindrome1 = self.get_palindrome(s, i-1, i)
            _length2, _palindrome2 = self.get_palindrome(s, i, i)
            if _length1 > longest_length:
                longest_length = _length1
                longest_palindrome = _palindrome1
            if _length2 > longest_length:
                longest_length = _length2
                longest_palindrome = _palindrome2
        return longest_palindrome

    def get_palindrome(self, s: str, left_center: int, right_center: int) -> (int, str):
        n = len(s)
        while s[left_center] == s[right_center]:
            left_center -= 1
            right_center += 1
            if not (0 <= left_center and right_center < n):
                break
        length = right_center - left_center - 1
        return length, s[left_center+1:right_center]
# @lc code=end
