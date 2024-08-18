from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic1 = Counter(nums1)
        dic2 = Counter(nums2)
        N = []
        # for val in nums1:
        #     if val in dic1:
        #         dic1[val] += 1
        #     else:
        #         dic1[val] = 1

        # for val2 in nums2:
        #     if val2 in dic2:
        #         dic2[val2] += 1
        #     else:
        #         dic2[val2] = 1

        for i in dic1:
            if i in dic2:
                N.extend([i] * min(dic1[i], dic2[i]))
        return N   