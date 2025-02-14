# Problem: Subarrays with K Different Integers - https://leetcode.com/problems/subarrays-with-k-different-integers/

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def helper(k):
            count = defaultdict(int)
            ans = 0
            left = 0
            for right in range(len(nums)):
                count[nums[right]] += 1
                while len(count) > k:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        del count[nums[left]]
                    
                    left += 1

                ans += right-left+1
            return ans
            
        val = helper (k)
        val2 = helper(k-1)
        return val-val2