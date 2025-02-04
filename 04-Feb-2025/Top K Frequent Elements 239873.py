# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        so = sorted(count.items(), key = lambda x: x[1], reverse=True)
        lst = []
        for i in range(k):
            lst.append(so[i][0])
        return lst