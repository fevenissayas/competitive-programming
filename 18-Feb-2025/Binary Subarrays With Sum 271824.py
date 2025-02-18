# Problem: Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        dic = {0:1}
        prefix = 0
        count = 0
        for elem in nums:
            prefix += elem
            if prefix-goal in dic:
                count += dic[prefix-goal]
            
            if prefix not in dic:
                dic[prefix] = 0
            dic[prefix] += 1
        
        return count