#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        not_ok, ok = -1, len(nums) - 1
        while ok - not_ok > 1:
            mid = (not_ok + ok) // 2
            if nums[mid] > nums[ok]:
                not_ok = mid
            else:
                ok = mid
        return nums[ok]
# @lc code=end
