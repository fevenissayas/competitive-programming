# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        lst = deque([i for i in range(1, n+1)])
        count = 1
        while len(lst) > 1:
            if count % k:
                lst.append(lst[0])
            lst.popleft()
            count += 1
            
        return lst[0]