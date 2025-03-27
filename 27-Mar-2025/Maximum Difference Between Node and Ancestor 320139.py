# Problem: Maximum Difference Between Node and Ancestor - https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        max_val = [float('-inf')]
        def helper(node, maxx, minn):
            if not node:
                max_val[0] = max(max_val[0], maxx - minn)
                return
            
            maxx = max(maxx, node.val)
            minn = min(minn, node.val)

            helper(node.left, maxx, minn)
            helper(node.right, maxx, minn)
        
            return max_val[0]
        return helper(root, float('-inf'), float('inf'))