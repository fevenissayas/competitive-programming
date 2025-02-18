# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dic = {0:1}
        prefix = 0
        count = 0
        for elem in nums:
            prefix += elem
            rem = prefix%k
            if rem in dic:
                count += dic[rem]
            
            if rem not in dic:
                dic[rem] = 0
            dic[rem] += 1
        
        return count