class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        lst1 = []
        lst2 = []
        for i in nums:
            if i % 2 == 0:
                lst1.append (i)        
            else:
                lst2.append (i)
        #lst1 += lst2
        return lst1 + lst2 