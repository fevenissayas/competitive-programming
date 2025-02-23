# Problem: Shuffle the Array - https://leetcode.com/problems/shuffle-the-array/

class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        answer = []
        for i in range(n):
            answer.append(nums[i])
            answer.append(nums[i + n])
        return answer
