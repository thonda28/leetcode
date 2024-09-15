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

        count_buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in num_to_count.items():
            count_buckets[count].append(num)
        flatten_count_buckets = [num for bucket in count_buckets for num in bucket]
        if len(flatten_count_buckets) < k:
            raise RuntimeError(f"The number of answers is fewer than the required {k}.")
        return flatten_count_buckets[-k:]
# @lc code=end
