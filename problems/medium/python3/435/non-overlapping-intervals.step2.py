#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#
# [Step2]
# 修正内容：
# 1. intervals が空の場合は 0 を返す（不要な interval の数を知りたいユースケースと関数名から判断）
# 2. 元の intervals に影響を与えないよう別の変数 sorted_intervals を使用
# 3. end 基準で考えるとシンプルになるのでソートを end 基準に変更
#
# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        sorted_intervals = sorted(intervals, key=lambda x: x[1])
        excluded_interval_count = 0
        _, prev_end = sorted_intervals[0]
        for i in range(1, len(sorted_intervals)):
            curr_start, curr_end = sorted_intervals[i]
            if curr_start < prev_end:
                excluded_interval_count += 1
            else:
                prev_end = curr_end
        return excluded_interval_count
# @lc code=end
