# Problem: Odd Even Linked List - https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        end = head
        ans = head
        count = 0
        if head == None or head.next == None:
            return head

        while end.next != None:
            end = end.next
            count += 1

        while count > 0:
            end.next = head.next
            end = end.next
            head.next = head.next.next
            head = head.next
            count -= 2
        
        end.next = None
        return ans