class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dI = Counter(nums).items() 
        result = []
        for num, count in dI:
            if count > len(nums) // 3:
                result.append(num)
        return result