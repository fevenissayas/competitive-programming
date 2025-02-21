# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        count = 0
        while temp != None:
            count += 1
            temp = temp.next

        dummy = ListNode()
        dummy.next = head
        pointer = dummy

        m = count-n+1
        val = 1
        while pointer.next:
            if val == m:
                pointer.next = pointer.next.next
            else:
                pointer = pointer.next
            val += 1

        return dummy.next
