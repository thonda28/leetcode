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
        if (m == 1) and (n == 1):
            return board[0][0] == word

        word_exists = False

        def isInside(row: int, col: int) -> bool:
            return (0 <= row < m) and (0 <= col < n)

        def search(row: int, col: int, index: int) -> bool:
            if index == len(word):
                nonlocal word_exists
                word_exists = True
                return

            if board[row][col] != word[index]:
                return

            tmp = board[row][col]
            board[row][col] = "#"
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if not isInside(row + dr, col + dc):
                    continue
                search(row + dr, col + dc, index + 1)
            board[row][col] = tmp

        for row in range(m):
            for col in range(n):
                search(row, col, 0)
        return word_exists
# @lc code=end
