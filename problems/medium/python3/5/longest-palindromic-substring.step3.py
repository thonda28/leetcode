#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        longest = s[0]
        for offset in range(2):
            for i in range(n):
                palindrome = self.get_palindrome(s, i, i + offset)
                if len(palindrome) > len(longest):
                    longest = palindrome
        return longest

    def get_palindrome(self, s: str, left: int, right: int) -> str:
        n = len(s)
        while 0 <= left and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
# @lc code=end
