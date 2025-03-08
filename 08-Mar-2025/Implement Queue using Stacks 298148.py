# Problem: Implement Queue using Stacks - https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue(object):

    def __init__(self):
        self.lst = []
        self.lst2 = []
        self.size = 0

    def push(self, x):
        self.lst.append (x)
        self.size += 1
        
    def pop(self):
        self.peek()
        return self.lst2.pop()
        
    def peek(self):
        if not self.lst2:
            while self.lst:
                self.lst2.append (self.lst.pop ())
            
        return self.lst2 [-1]
            
        
    def empty(self):
        return not self.lst2 and not self.lst
        


#Your MyQueue object will be instantiated and called as such:
#obj = MyQueue()
#obj.push("hey")
#obj.push ("bye")
#param_2 = obj.pop()
#param_3 = obj.peek()
#param_4 = obj.empty()