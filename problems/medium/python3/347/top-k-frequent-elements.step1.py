#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_count = dict()
        for num in nums:
            if num not in num_to_count:
                num_to_count[num] = 0
            num_to_count[num] += 1

        # Since heapq.heappop() extracts the smallest value,
        # multiplying by -1 is used to retrieve the maximum value.
        freq_num_list = [(-value, key) for key, value in num_to_count.items()]
        heapq.heapify(freq_num_list)
        most_frequent_elements = []
        for _ in range(k):
            _, element = heapq.heappop(freq_num_list)
            most_frequent_elements.append(element)
        return most_frequent_elements
# @lc code=end
