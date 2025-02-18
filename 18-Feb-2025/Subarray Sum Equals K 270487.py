# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = {0:1}
        prefix = 0
        count = 0
        for elem in nums:
            prefix += elem
            if prefix-k in dic:
                count += dic[prefix-k]
            
            if prefix not in dic:
                dic[prefix] = 0
            dic[prefix] += 1
        
        return count