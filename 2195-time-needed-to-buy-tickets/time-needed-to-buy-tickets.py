class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque(range(len(tickets)))
        val = 0
        while tickets[k]:
            i = queue.popleft()
            if tickets[i] > 0:
                tickets[i] -= 1
                val += 1
            queue.append(i)
            
        return val