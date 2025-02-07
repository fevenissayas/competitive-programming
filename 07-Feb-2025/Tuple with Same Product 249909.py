# Problem: Tuple with Same Product - http://leetcode.com/problems/tuple-with-same-product

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:        
        n = len(nums)
        dict_ = defaultdict(int)
        ans = 0

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                dict_[nums[i]*nums[j]] += 1

        for val in dict_.values():
            ans += 8 * (val * (val-1))//2

        return ans