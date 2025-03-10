# Problem: Longest Contiguous Subarray With Absolute Diff Less Than or Equal to Limit - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxq = deque()
        minq = deque()
        n = len(nums)
        j = 0
        ans = 0
        for i in range(n):
            while maxq and nums[i] > maxq[-1]:
                maxq.pop()
            maxq.append(nums[i])
            while minq and nums[i] < minq[-1]:
                minq.pop()
            minq.append(nums[i])
            if maxq[0] - minq[0] > limit:
                if nums[j] == maxq[0]:
                    maxq.popleft()
                if nums[j] == minq[0]:
                    minq.popleft()
                j += 1
            ans = max(ans, i - j + 1)
        return ans
