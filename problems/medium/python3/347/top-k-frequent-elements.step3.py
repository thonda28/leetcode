#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
T = TypeVar('T')


class MyMaxHeap:
    def __init__(self, items: List[T]):
        self.tree = []
        for item in items:
            self.push(item)

    def push(self, item: T):
        self.tree.append(item)
        last_index = len(self.tree) - 1
        self._sift_up()

    def _sift_up(self):
        child = len(self.tree) - 1
        while child:
            parent = (child - 1) // 2
            if self.tree[parent] >= self.tree[child]:
                break
            self.tree[parent], self.tree[child] = self.tree[child], self.tree[parent]
            child = parent

    def pop(self) -> T:
        top_item = self.tree[0]
        last_item = self.tree.pop()
        if self.tree:
            self.tree[0] = last_item
            self._sift_down()
        return top_item

    def _sift_down(self):
        parent = 0
        while 2 * parent + 1 < len(self.tree):
            child = 2 * parent + 1
            right_child = child + 1
            if right_child < len(self.tree) and self.tree[child] < self.tree[right_child]:
                child = right_child
            if self.tree[parent] >= self.tree[child]:
                break
            self.tree[parent], self.tree[child] = self.tree[child], self.tree[parent]
            parent = child


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_count = dict()
        for num in nums:
            if num not in num_to_count:
                num_to_count[num] = 0
            num_to_count[num] += 1

        count_num_list = [(count, num) for num, count in num_to_count.items()]
        heap = MyMaxHeap(count_num_list)
        most_frequent_elements = []
        for _ in range(k):
            _, num = heap.pop()
            most_frequent_elements.append(num)
        return most_frequent_elements
# @lc code=end
