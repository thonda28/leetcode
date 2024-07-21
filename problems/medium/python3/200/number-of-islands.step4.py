#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class UnionFind:
    def __init__(self, n: int):
        self.roots = list(range(n))
        self.ranks = [0] * n

    def find_root(self, node: int) -> int:
        if self.roots[node] == node:
            return node
        self.roots[node] = self.find_root(self.roots[node])
        return self.roots[node]

    def unite(self, node1: int, node2: int) -> bool:
        root1 = self.find_root(node1)
        root2 = self.find_root(node2)
        if root1 == root2:
            return False

        if self.ranks[root1] < self.ranks[root2]:
            root1, root2 = root2, root1
        self.roots[root2] = root1
        if self.ranks[root1] == self.ranks[root2]:
            self.ranks[root1] += 1
        return True


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def is_inside(row: int, col: int) -> bool:
            return 0 <= row < m and 0 <= col < n

        def calc_node(row: int, col: int) -> int:
            return row * n + col

        m = len(grid)
        n = len(grid[0])
        num_islands = m * n
        uf = UnionFind(m * n)
        for row in range(m):
            for col in range(n):
                if grid[row][col] == '0':
                    num_islands -= 1
                    continue

                node = calc_node(row, col)
                if is_inside(row, col + 1) and grid[row][col + 1] == '1':
                    right_node = calc_node(row, col + 1)
                    if uf.unite(node, right_node):
                        num_islands -= 1
                if is_inside(row + 1, col) and grid[row + 1][col] == '1':
                    lower_node = calc_node(row + 1, col)
                    if uf.unite(node, lower_node):
                        num_islands -= 1
        return num_islands
# @lc code=end
