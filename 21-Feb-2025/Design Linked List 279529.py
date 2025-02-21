# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class Node:
    def __init__(self, val = 0 , next = None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.head = Node()
    def get(self, index: int) -> int:
        curr = self.head
        curr_index = 0
        while curr is not None and curr_index <= index:
            curr = curr.next
            curr_index +=1
        if curr:
            return curr.val
        else:
            return -1
    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head.next
        self.head.next = new_node
        return self.head

    def addAtTail(self, val: int) -> None:
        curr= self.head
        while curr and curr.next:
            curr = curr.next
        new_node = Node(val)
        curr.next = new_node
        return self.head

    def addAtIndex(self, index: int, val: int) -> None:
        new_node = Node(val)

        curr = self.head
        curr_index = 0
        if index < 0:
            return self.head
       
        while curr_index < index and curr:
            curr = curr.next
            curr_index +=1

        if curr:
            new_node.next = curr.next
            curr.next = new_node
        
        return self.head

    def deleteAtIndex(self, index: int) -> None:
        
        curr = self.head
        curr_index = 0

        if not curr and not curr.next:
            return self.head

        while curr_index < index and curr:
            curr = curr.next
            curr_index +=1

        if curr and curr.next:
            if curr.next.next is  None:
                curr.next = None
            else:
                curr.next = curr.next.next
        return self.head



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
