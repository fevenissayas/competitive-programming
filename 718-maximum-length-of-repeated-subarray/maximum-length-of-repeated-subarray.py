class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        maxi = 0
        for i in range(len(nums1)):
            val = 0
            for j in range(min(len(nums1)-i, len(nums2))):
                if nums1[i+j] == nums2[j]:
                    val += 1
                    maxi = max(val, maxi)
                else:
                    val = 0
        
        for i in range(len(nums2)):
            val = 0
            for j in range(min(len(nums1), len(nums2)-i)):
                if nums2[i+j] == nums1[j]:
                    val += 1
                    maxi = max(val, maxi)
                else:
                    val = 0

        return maxi
