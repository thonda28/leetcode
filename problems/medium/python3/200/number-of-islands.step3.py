#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def is_inside(row: int, col: int) -> bool:
            return 0 <= row < m and 0 <= col < n

        def is_unvisited_island(row: int, col: int) -> bool:
            return grid[row][col] == "1" and (row, col) not in visited

        def explore(start_row: int, start_col: int) -> None:
            points = [(start_row, start_col)]
            while points:
                row, col = points.pop()
                if not is_inside(row, col):
                    continue
                if not is_unvisited_island(row, col):
                    continue

                visited.add((row, col))
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    points.append((row + dr, col + dc))

        visited = set()
        num_islands = 0
        for row in range(m):
            for col in range(n):
                if is_unvisited_island(row, col):
                    num_islands += 1
                    explore(row, col)
        return num_islands
# @lc code=end
