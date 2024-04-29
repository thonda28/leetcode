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
        kth_smallest = 0

        def search_inorder(root: Optional[TreeNode]):
            nonlocal k, kth_smallest
            if not root:
                return
            search_inorder(root.left)
            k -= 1
            if k == 0:
                kth_smallest = root.val
                return
            search_inorder(root.right)

        search_inorder(root)
        return kth_smallest
# @lc code=end
