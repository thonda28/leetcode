#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#
# [Step1] 12分で Pass
# 時間計算量：O(NlogN)、空間計算量：O(1)
# 方針：
# intervals をソートして、prev_end と curr_start が重複しているかを見ていく
# prev_start <= curr_start は自明だが、prev_end <= curr_end は言えないことに気づかず
# 一度 Wrong Answer になった（その後、重複時は end が小さいもので更新する処理を追加）
#
# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        excluded_interval_count = 0
        prev_start, prev_end = intervals[0]
        for i in range(1, len(intervals)):
            curr_start, curr_end = intervals[i]
            if prev_end <= curr_start:
                prev_start = curr_start
                prev_end = curr_end
            else:
                if prev_end > curr_end:
                    prev_start = curr_start
                    prev_end = curr_end
                excluded_interval_count += 1
        return excluded_interval_count
# @lc code=end
