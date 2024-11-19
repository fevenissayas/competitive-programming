class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # [1,2,2,3,8]
        # [0,1,2,3,4]
#optimized

        numss = sorted(nums)
        s = {}
        for i in range(len(nums)):
            if numss[i] not in s:
                s[numss[i]] = i
        return [s[num] for num in nums]
# time complexity: O(nlogn)
#SPACE COMPLEXITY: O(n)

#brute force
        # lst = []
        # for i in range(len(nums)): O(N)
        #     v = 0
        #     for j in range(len(nums)):O(N)
        #         if nums[i] > nums[j]:
        #             v += 1
        #     lst.append(v)
        # return lst
    
# time complexity == O(n2)
# space complexity == O(n)

