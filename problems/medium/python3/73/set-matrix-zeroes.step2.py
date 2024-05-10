#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        first_row_has_zero = any([matrix[0][col] == 0 for col in range(n)])
        first_col_has_zero = any([matrix[row][0] == 0 for row in range(m)])

        for row in range(1, m):
            for col in range(1, n):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        for row in range(1, m):
            for col in range(1, n):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0

        if first_row_has_zero:
            for col in range(n):
                matrix[0][col] = 0
        if first_col_has_zero:
            for row in range(m):
                matrix[row][0] = 0
# @lc code=end
