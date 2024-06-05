#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node = root
        while node:
            if node == p or node == q:
                return node
            if p.val < node.val and q.val < node.val:
                node = node.left
                continue
            if node.val < p.val and node.val < q.val:
                node = node.right
                continue
            return node
# @lc code=end
