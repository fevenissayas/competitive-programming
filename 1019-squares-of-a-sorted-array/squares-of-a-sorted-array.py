class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums) - 1
        lst = []
        
        while i <= j:
            if abs(nums[i]) > abs(nums[j]):
                lst.append(nums[i] ** 2)
                i += 1
            else:
                lst.append(nums[j] ** 2)
                j -= 1

        return lst[::-1]