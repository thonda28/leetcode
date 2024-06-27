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

        def search(start_row: int, start_col: int) -> bool:
            visited = set()
            candidates = [(start_row, start_col, 0, visited)]
            while candidates:
                row, col, index, visited = candidates.pop()
                if not is_inside(row, col):
                    continue
                if board[row][col] != word[index]:
                    continue
                if (row, col) in visited:
                    continue
                if index == len(word) - 1:
                    return True

                copied_visited = deepcopy(visited)
                copied_visited.add((row, col))
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    candidates.append((row + dr, col + dc, index + 1, copied_visited))
            return False

        for row in range(m):
            for col in range(n):
                if search(row, col):
                    return True
        return False
# @lc code=end
