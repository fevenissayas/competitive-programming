class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        #sort
        max_num = max(costs)
        count = [0]*(max_num + 1)
        for i in costs:
            count[i] += 1
        summ = 0
        for i in range(1,max_num+1):
            summ = count[i] + count[i-1]
            count[i] = summ
        
        arr = [0]*len(costs)
        k = len(costs) - 1
        while k>= 0:
            arr[count[costs[k]] - 1] = costs[k]
            count[costs[k]] -= 1
            k -= 1

        j = 0
        for i, val in enumerate(arr):
            j += val
            if j > coins:                      
                return i
        return len(arr)