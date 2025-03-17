# Problem:  Insert into a Binary Search Tree - https://leetcode.com/problems/insert-into-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def search(node, value):
            if not node:
                return TreeNode(value)
            
            if node.val < value:
                node.right = search(node.right, value)
            else:
                node.left = search(node.left, value) # New node

            return node
        
        return search(root, val)