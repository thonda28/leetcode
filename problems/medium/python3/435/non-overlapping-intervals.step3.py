#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#
# [Step3]
# 修正内容：
# いただいたコメントに基づいて以下のように変数名を修正
# - `prev_end` -> `last_end`
# - `curr_start` -> `start`
# - `curr_end` -> `end`
#
# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        sorted_intervals = sorted(intervals, key=lambda x: x[1])
        excluded_interval_count = 0
        _, last_end = sorted_intervals[0]
        for i in range(1, len(sorted_intervals)):
            start, end = sorted_intervals[i]
            if start < last_end:
                excluded_interval_count += 1
            else:
                last_end = end
        return excluded_interval_count
# @lc code=end
