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
        row_has_zero = [False] * m
        col_has_zero = [False] * n

        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    row_has_zero[row] = True
                    col_has_zero[col] = True

        for row in range(m):
            for col in range(n):
                if row_has_zero[row] or col_has_zero[col]:
                    matrix[row][col] = 0
# @lc code=end
