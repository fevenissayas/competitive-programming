# Problem: LRU Cache - https://leetcode.com/problems/lru-cache/

class Node:
    def __init__(self, val, key):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.Dummy_head, self.Dummy_tail = Node('Dummy',0), Node('Dummy',0)
        self.Dummy_head.next = self.Dummy_tail
        self.Dummy_tail.prev = self.Dummy_head
        self.capacity = capacity
        self.lru_dic = {}

    def insert_at_the_end(self, node):
        old_tail = self.Dummy_tail.prev
        old_tail.next = node
        node.prev = old_tail
        self.Dummy_tail.prev = node
        node.next = self.Dummy_tail

    def delete_node(self, node):
        previous_node = node.prev
        next_node = node.next
        previous_node.next = next_node
        next_node.prev = previous_node

    def get(self, key: int) -> int:
        if key in self.lru_dic:
            node = self.lru_dic[key]
            self.delete_node(node)
            self.insert_at_the_end(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.lru_dic:
            node = self.lru_dic[key]
            self.delete_node(node)
            node.val = value
            self.insert_at_the_end(node)
            self.lru_dic[key] = node
        else:
            if len(self.lru_dic) == self.capacity:
                lru_node = self.Dummy_head.next
                self.delete_node(lru_node)
                del self.lru_dic[lru_node.key]

            new_node = Node(value, key)
            self.insert_at_the_end(new_node)
            self.lru_dic[key] = new_node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
