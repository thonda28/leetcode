#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#

# @lc code=start
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        canFlowToPacificOcean = [[False for _ in range(n)] for _ in range(m)]
        canFlowToAtlanticOcean = [[False for _ in range(n)] for _ in range(m)]

        self._canFlowBackFromPacificOcean(heights, canFlowToPacificOcean)
        self._canFlowBackFromAtlanticOcean(heights, canFlowToAtlanticOcean)

        canFlowToBothOcean = []
        for row in range(m):
            for col in range(n):
                if canFlowToPacificOcean[row][col] and canFlowToAtlanticOcean[row][col]:
                    canFlowToBothOcean.append([row, col])
        return canFlowToBothOcean

    def _canFlowBackFromPacificOcean(self, heights: List[List[int]], canFlowToPacificOcean: List[List[int]]):
        m, n = len(heights), len(heights[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        canFlowCells = []
        for row in range(m):
            canFlowCells.append((row, 0))
        for col in range(n):
            canFlowCells.append((0, col))

        while canFlowCells:
            row, col = canFlowCells.pop()
            if visited[row][col]:
                continue
            visited[row][col] = True
            canFlowToPacificOcean[row][col] = True

            for _row, _col in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
                if _row < 0 or m <= _row or _col < 0 or n <= _col:
                    continue
                if visited[_row][_col]:
                    continue
                if heights[_row][_col] >= heights[row][col]:
                    canFlowCells.append((_row, _col))

    def _canFlowBackFromAtlanticOcean(self, heights: List[List[int]], canFlowToAtlanticOcean: List[List[int]]):
        m, n = len(heights), len(heights[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        canFlowCells = []
        for row in range(m):
            canFlowCells.append((row, n-1))
        for col in range(n):
            canFlowCells.append((m-1, col))

        while canFlowCells:
            row, col = canFlowCells.pop()
            if visited[row][col]:
                continue
            visited[row][col] = True
            canFlowToAtlanticOcean[row][col] = True

            for _row, _col in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
                if _row < 0 or m <= _row or _col < 0 or n <= _col:
                    continue
                if visited[_row][_col]:
                    continue
                if heights[_row][_col] >= heights[row][col]:
                    canFlowCells.append((_row, _col))

# @lc code=end
