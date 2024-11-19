from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # brute force
        # min_num = min(nums1, nums2)
        # max_num = max(nums1, nums2)
        # lst = []
        # for i in range(len(max_num)):
        #     if max_num[i] in min_num:
        #         lst.append(max_num[i])
        #         min_num.remove(max_num[i])
        # return lst
        
        count = Counter (nums2)
        lst = []
        for i, val in enumerate(nums1):
            if count[val]:
                lst.append(val)
                count[val] -= 1
        return lst
