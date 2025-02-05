# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        lst = [0]*len(nums)
        s = 0
        for even in nums:
            if even % 2 == 0:
                s += even

        j = 0
        for elem in queries:
            left = elem[0]
            right = elem[1]
            
            if nums[right]%2 and elem[0]%2:
                nums[right] += left
                s += nums[right]
            elif nums[right]%2 == 0 and left%2 == 0:
                nums[right] += left
                s += left
            elif nums[right]%2 == 0 and left%2:
                s -= nums[right]
                nums[right] += left
            else:
                nums[right] += left
                
            lst[j] = s
            j += 1

        return lst