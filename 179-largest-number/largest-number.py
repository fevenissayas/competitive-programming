class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # lst = []
        # for num in nums:
        #     for dig in str(num):
        #         lst.append(int(dig))
        
        # for i in range(len(lst)):
        #     for j in range(1, len(lst)):
        #         if lst[j] > lst [j-1]:
        #             lst[j], lst[j-1] = lst[j-1], lst[j]
        # lst =''.join(map(str, lst))
        # return lst

        nums = list(map(str, nums))
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] < nums[j] + nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
        nums = ''.join(nums)
        
        return '0' if nums[0] == '0' else nums