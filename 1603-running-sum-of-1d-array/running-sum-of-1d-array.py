class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        lst = []
        summ = 0
        for i in range(len(nums)):
            summ += nums[i]
            lst.append(summ)        
        
        return lst