#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        longest_palindrome = s[0]
        for i in range(1, n):
            even_palindrome = self.get_palindrome(s, i - 1, i)
            odd_palindrome = self.get_palindrome(s, i, i)
            if len(even_palindrome) > len(longest_palindrome):
                longest_palindrome = even_palindrome
            if len(odd_palindrome) > len(longest_palindrome):
                longest_palindrome = odd_palindrome
        return longest_palindrome

    def get_palindrome(self, s: str, left: int, right: int) -> str:
        n = len(s)
        while 0 <= left and right < n:
            if s[left] != s[right]:
                break
            left -= 1
            right += 1
        return s[left + 1:right]
# @lc code=end
