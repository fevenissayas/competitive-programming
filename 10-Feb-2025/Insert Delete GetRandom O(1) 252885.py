# Problem: Insert Delete GetRandom O(1) - https://leetcode.com/problems/insert-delete-getrandom-o1/description/

class RandomizedSet:

    def __init__(self):
        self.dic = {}
        self.lst = []

    def insert(self, val: int) -> bool:
        if val not in self.dic:
            self.lst.append(val)
            self.dic[val] = len(self.lst) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.dic:
            idx = self.dic[val]
            self.lst[idx], self.lst[-1] = self.lst[-1], self.lst[idx]
            self.dic[self.lst[idx]] = idx

            del(self.dic[val])
            self.lst.pop()
            return True
        return False

    def getRandom(self) -> int:
        rand = random.randint(0, len(self.lst)-1)
        return self.lst[rand]