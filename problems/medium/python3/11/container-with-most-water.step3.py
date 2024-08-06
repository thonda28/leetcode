#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
import bisect
from typing import List, Tuple


class Solution:
    def maxArea(self, height: List[int]) -> int:

        def generate_necessary_height_with_indices(height: List[int], reverse: bool) -> List[Tuple[int, int]]:
            start, stop, step = (n - 1, -1, -1) if reverse else (0, n, 1)

            necessary_height_with_indices = [(-1, -1)]
            for i in range(start, stop, step):
                if necessary_height_with_indices[-1][0] < height[i]:
                    necessary_height_with_indices.append((height[i], i))
            return necessary_height_with_indices

        n = len(height)
        max_amount = 0

        necessary_right_height_with_indices = generate_necessary_height_with_indices(height, reverse=True)
        for left in range(n):
            i = bisect.bisect_left(
                necessary_right_height_with_indices,
                True,
                key=lambda x: x[0] >= height[left]
            )
            right = necessary_right_height_with_indices[i][1]
            max_amount = max(max_amount, (right - left) * height[left])

        necessary_left_height_with_indices = generate_necessary_height_with_indices(height, False)
        for right in range(n - 1, -1, -1):
            i = bisect.bisect_left(
                necessary_left_height_with_indices,
                True,
                key=lambda x: x[0] >= height[right]
            )
            left = necessary_left_height_with_indices[i][1]
            max_amount = max(max_amount, (right - left) * height[right])

        return max_amount
# @lc code=end
