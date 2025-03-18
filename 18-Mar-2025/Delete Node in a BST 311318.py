# Problem: Delete Node in a BST - https://leetcode.com/problems/delete-node-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def find_min(node):
            while node.left:
                node = node.left
            return node

        def search(node, key):
            if not node:
                return
            if node.val > key:
                node.left = search(node.left, key)
            elif node.val < key:
                node.right = search(node.right, key)
            else:
                if not node.right:
                    return node.left
                elif not node.left:
                    return node.right
                else:
                    succ = find_min(node.right)
                    node.val = succ.val
                    succ.val = key
                    node.right = search(node.right, key)
            
            return node
        
        return search(root, key)