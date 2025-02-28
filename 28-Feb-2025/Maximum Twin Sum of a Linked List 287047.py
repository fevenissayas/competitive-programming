# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        max_sum = 0
        while head !=  mid:
            max_sum = max(max_sum, prev.val+head.val)
            prev = prev.next
            head = head.next
        
        return max_sum