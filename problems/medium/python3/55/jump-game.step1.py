#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        can_reach = [False] * n
        can_reach[0] = True
        for i in range(n):
            if can_reach[i]:
                width = nums[i]
                can_reach[i + 1:i + width + 1] = [True] * width
        return can_reach[n - 1]
# @lc code=end
