# Problem: Maximum Sum Obtained of Any Permutation - https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/description/

class Solution:
    def maxSumRangeQuery(self, nums: List[int], req: List[List[int]]) -> int:
        n = len(nums)
        diff = [0] * n   
        for s, e in req:
            diff[s] += 1
            if e + 1 < n:
                diff[e + 1] -= 1
                
        for i in range(1, n):
            diff[i] += diff[i - 1]
            
        nums.sort()
        diff.sort()
        total = 0
        mod = 10**9 + 7
        
        for i in range(n):
            total += nums[i] * diff[i]
            
        return total % mod