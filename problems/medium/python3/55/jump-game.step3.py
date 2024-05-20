#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable_index = nums[0]
        for i in range(1, len(nums)):
            if reachable_index < i:
                return False
            reachable_index = max(reachable_index, i + nums[i])
        return True
# @lc code=end
