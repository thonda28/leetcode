#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        reachable_index = nums[0]
        for i in range(1, n):
            if i > reachable_index:
                break
            reachable_index = max(reachable_index, i + nums[i])
        return reachable_index >= n - 1
# @lc code=end
