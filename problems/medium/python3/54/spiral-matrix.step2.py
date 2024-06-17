#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        def get_spiral_order(spiral_order: List[int], mode: int) -> List[int]:
            nonlocal top, bottom, left, right
            if not (top <= bottom and left <= right):
                return spiral_order

            match mode:
                case 0: # top
                    for col in range(left, right + 1):
                        spiral_order.append(matrix[top][col])
                    top += 1
                case 1: # right
                    for row in range(top, bottom + 1):
                        spiral_order.append(matrix[row][right])
                    right -= 1
                case 2: # bottom
                    for col in range(right, left - 1, -1):
                        spiral_order.append(matrix[bottom][col])
                    bottom -= 1
                case 3: # left
                    for row in range(bottom, top - 1, - 1):
                        spiral_order.append(matrix[row][left])
                    left += 1
            return get_spiral_order(spiral_order, (mode + 1) % 4)

        return get_spiral_order([], 0)
# @lc code=end
