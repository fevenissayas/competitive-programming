# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        summ = [0]
        def helper(node, ans):
            if not node.left and not node.right:
                ans.append(node.val)
                summ[0] += int(''.join(map(str, ans)))
                return
            
            ans.append(node.val)
            
            if node.left:
                helper(node.left, ans[:])
            if node.right:
                helper(node.right, ans[:])
        
        helper(root, [])
        return summ[0]