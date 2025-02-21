# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
           slow = slow.next
           fast = fast.next.next
        
        new_node = None
        temp = slow
        
        while temp:
            var = temp.next
            temp.next = new_node
            new_node = temp
            temp = var
        
        while new_node and head:
            if new_node.val != head.val:
                return False
            new_node = new_node.next
            head = head.next
        
        return True
    