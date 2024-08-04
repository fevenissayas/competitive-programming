class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        modulo = 10**9 + 7
        arr = []
        
        for i in range(n):
            s = 0
            for j in range(i, n):
                s += nums[j]
                arr.append(s)
        arr.sort()

        return sum(arr[left - 1 : right]) % modulo