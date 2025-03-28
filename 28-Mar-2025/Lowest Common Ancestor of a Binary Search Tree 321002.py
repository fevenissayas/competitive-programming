# Problem: Lowest Common Ancestor of a Binary Search Tree - https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(node, p, q):
            if node.val > p.val and node.val > q.val: 
                return helper(node.left, p, q) 
            elif node.val < p.val and node.val < q.val:
                return helper(node.right, p, q)
            else:
                return node
        
        return helper(root, p, q)