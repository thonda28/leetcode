#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def is_inside(row: int, col: int) -> bool:
            return (0 <= row < m) and (0 <= col < n)

        def search(row: int, col: int, index: int) -> bool:
            if board[row][col] != word[index]:
                return False
            if index == len(word) - 1:
                return True

            tmp = board[row][col]
            board[row][col] = "#"

            word_exists = False
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if not is_inside(row + dr, col + dc):
                    continue
                word_exists |= search(row + dr, col + dc, index + 1)

            board[row][col] = tmp
            return word_exists

        for row in range(m):
            for col in range(n):
                if search(row, col, 0):
                    return True
        return False
# @lc code=end
