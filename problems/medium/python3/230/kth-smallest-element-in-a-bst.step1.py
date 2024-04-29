#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ascending_list = []

        def search_inorder(root: Optional[TreeNode]):
            if not root:
                return
            search_inorder(root.left)
            ascending_list.append(root.val)
            search_inorder(root.right)

        search_inorder(root)
        return ascending_list[k - 1]
# @lc code=end
