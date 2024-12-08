class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """

        t = 3
        [1,2],[3]


        [2,3,1,2,4,3]

        [2]
        [2,3]
        [2,3,1]

        sum += arr[j]

2
1
2

1

nums = [1,1,1,1,1,1,1,1]


        """
        var = 0
        le = float('inf')
        j = 0
        # if sum(nums) < target:
        #     return 0
        for i in range(len(nums)):
            var += nums[i]
            while var >= target:
                le = min(le, i - j + 1)
                var -= nums[j]
                j += 1

        return le if le != float('inf') else 0