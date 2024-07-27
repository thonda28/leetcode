#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class RangeMaximumQuerySegmentTree:
    def __init__(self, nums: List[int], min_value: int):
        self.min_value = min_value
        x = 1
        while x < len(nums):
            x *= 2
        self.n = x
        self.tree = [self.min_value] * (2 * self.n - 1)

        for index, num in enumerate(nums):
            self.update(index, num)

    def update(self, index: int, value: int):
        index += self.n - 1
        self.tree[index] = value
        while index > 0:
            index = (index - 1) // 2
            self.tree[index] = max(self.tree[2 * index + 1], self.tree[2 * index + 2])

    def range_maximum_query(self, begin: int, end: int) -> int:
        return self.__sub_query(begin, end, 0, 0, self.n)

    def __sub_query(self, begin: int, end: int, index: int, left: int, right: int) -> int:
        if end <= left or right <= begin:
            return self.min_value
        if begin <= left and right <= end:
            return self.tree[index]
        mid = (left + right) // 2
        val1 = self.__sub_query(begin, end, index * 2 + 1, left, mid)
        val2 = self.__sub_query(begin, end, index * 2 + 2, mid, right)
        return max(val1, val2)
# @lc code=end
