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

        def is_unvisited_island(row: int, col: int, visited: Set[Tuple[int]]) -> bool:
            return ((row, col) not in visited) and (grid[row][col] == "1")

        def is_inside(row: int, col: int) -> bool:
            return (0 <= row < m) and (0 <= col < n)

        def explore(row: int, col: int, visited: Set[Tuple[int]]):
            if not is_unvisited_island(row, col, visited):
                return

            visited.add((row, col))
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if not is_inside(row + dr, col + dc):
                    continue
                explore(row + dr, col + dc, visited)

        visited = set()
        num_islands = 0
        for row in range(m):
            for col in range(n):
                if is_unvisited_island(row, col, visited):
                    num_islands += 1
                    explore(row, col, visited)
        return num_islands
# @lc code=end
