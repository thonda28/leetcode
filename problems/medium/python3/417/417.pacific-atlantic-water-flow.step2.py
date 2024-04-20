#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#

# @lc code=start
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        can_flow_to_pacific = [[False for _ in range(n)] for _ in range(m)]
        can_flow_to_atlantic = [[False for _ in range(n)] for _ in range(m)]

        for row in range(m):
            self._can_flow_back_from_ocean(heights, can_flow_to_pacific, row, 0)
            self._can_flow_back_from_ocean(heights, can_flow_to_atlantic, row, n-1)
        for col in range(n):
            self._can_flow_back_from_ocean(heights, can_flow_to_pacific, 0, col)
            self._can_flow_back_from_ocean(heights, can_flow_to_atlantic, m-1, col)

        can_flow_to_both = []
        for row in range(m):
            for col in range(n):
                if can_flow_to_pacific[row][col] and can_flow_to_atlantic[row][col]:
                    can_flow_to_both.append([row, col])
        return can_flow_to_both

    def _can_flow_back_from_ocean(self, heights: List[List[int]], can_flow_to_ocean: List[List[int]], row: int, col: int):
        can_flow_to_ocean[row][col] = True
        m, n = len(heights), len(heights[0])
        for _row, _col in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
            if _row < 0 or m <= _row or _col < 0 or n <= _col:
                continue
            if can_flow_to_ocean[_row][_col]:
                continue
            if heights[_row][_col] >= heights[row][col]:
                self._can_flow_back_from_ocean(heights, can_flow_to_ocean, _row, _col)
# @lc code=end
