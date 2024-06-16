#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row_start = 0
        row_end = len(matrix) - 1
        col_start = 0
        col_end = len(matrix[0]) - 1

        spiral_order = []
        while row_start <= row_end and col_start <= col_end:
            # upper
            for col in range(col_start, col_end + 1):
                spiral_order.append(matrix[row_start][col])
            row_start += 1

            # right
            for row in range(row_start, row_end + 1):
                spiral_order.append(matrix[row][col_end])
            col_end -= 1

            # lower
            if row_start <= row_end:
                for col in range(col_end, col_start - 1, -1):
                    spiral_order.append(matrix[row_end][col])
                row_end -= 1

            # left
            if col_start <= col_end:
                for row in range(row_end, row_start - 1, - 1):
                    spiral_order.append(matrix[row][col_start])
                col_start += 1

        return spiral_order
# @lc code=end
