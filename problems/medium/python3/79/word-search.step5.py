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
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        found = False

        def is_inside(row: int, col: int) -> bool:
            return 0 <= row < m and 0 <= col < n

        def search(start_row: int, start_col: int):
            nonlocal found
            candidates = [(start_row, start_col, 0, 0)]
            while candidates:
                row, col, word_index, direction_index = candidates.pop()
                if direction_index == len(directions):
                    board[row][col] = word[word_index]
                    continue

                if direction_index == 0:
                    if board[row][col] != word[word_index]:
                        continue
                    if word_index == len(word) - 1:
                        found = True
                        return
                    board[row][col] = "#"

                dr, dc = directions[direction_index]
                candidates.append((row, col, word_index, direction_index + 1))
                if is_inside(row + dr, col + dc):
                    candidates.append((row + dr, col + dc, word_index + 1, 0))

        for row in range(m):
            for col in range(n):
                search(row, col)
        return found
# @lc code=end
