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
            return (0 <= row < m) and (0 <= col < n)

        def explore(row: int, col: int, visited: Set[Tuple[int]]) -> bool:
            if (row, col) in visited:
                return False
            if grid[row][col] != "1":
                return False

            is_island = True
            visited.add((row, col))
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if not is_inside(row + dr, col + dc):
                    continue
                is_island |= explore(row + dr, col + dc, visited)
            return is_island

        visited = set()
        num_islands = 0
        for row in range(m):
            for col in range(n):
                if explore(row, col, visited):
                    num_islands += 1
        return num_islands
# @lc code=end
