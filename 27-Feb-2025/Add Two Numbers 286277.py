# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = l1
        n2 = l2
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while n1 or n2 or carry:
            val = (n1.val if n1 else 0) + (n2.val if n2 else 0) + carry
            carry = val // 10
            current.next = ListNode(val % 10)
            current = current.next
            
            n1 = n1.next if n1 else None
            n2 = n2.next if n2 else None
        
        return dummy.next