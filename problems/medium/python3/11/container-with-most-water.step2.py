#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
import math
from typing import Callable, Iterable, List


class SegmentTree:
    def __init__(self, nums: List[int], func: Callable[[Iterable[int]], int], default_value: int):
        self.func = func
        self.default_value = default_value
        x = 1
        while x < len(nums):
            x *= 2
        self.n = x
        self.tree = [self.default_value] * (2 * self.n - 1)

        for index in range(len(nums)):
            self.update(index, nums[index])

    def update(self, index: int, value: int):
        index += self.n - 1
        self.tree[index] = value
        while index > 0:
            index = (index - 1) // 2
            self.tree[index] = self.func([self.tree[2 * index + 1], self.tree[2 * index + 2]])

    def range_query(self, begin: int, end: int) -> int:
        return self.__sub_query(begin, end, 0, 0, self.n)

    def __sub_query(self, begin: int, end: int, index: int, left: int, right: int) -> int:
        if end <= left or right <= begin:
            return self.default_value
        if begin <= left and right <= end:
            return self.tree[index]
        mid = (left + right) // 2
        val1 = self.__sub_query(begin, end, index * 2 + 1, left, mid)
        val2 = self.__sub_query(begin, end, index * 2 + 2, mid, right)
        return self.func([val1, val2])


class Solution:
    def swap_index_value(self, nums: List[int], use_last_seen: bool, default_value: int) -> List[int]:
        n = len(nums)
        swapped_list = [default_value] * (max(nums) + 1)
        start, stop, step = (0, n, 1) if use_last_seen else (n - 1, -1, -1)

        for index in range(start, stop, step):
            swapped_list[nums[index]] = index

        return swapped_list

    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        max_height = max(height)
        max_amount = 0

        last_seen_map = self.swap_index_value(height, use_last_seen=True, default_value=-math.inf)
        max_seg_tree = SegmentTree(last_seen_map, func=max, default_value=-math.inf)
        for left in range(n):
            left_height = height[left]
            right = max_seg_tree.range_query(left_height, max_height + 1)
            max_amount = max(max_amount, left_height * (right - left))

        first_seen_map = self.swap_index_value(height, use_last_seen=False, default_value=math.inf)
        min_seg_tree = SegmentTree(first_seen_map, func=min, default_value=math.inf)
        for right in range(n - 1, -1, -1):
            right_height = height[right]
            left = min_seg_tree.range_query(right_height, max_height + 1)
            max_amount = max(max_amount, right_height * (right - left))

        return max_amount
# @lc code=end
