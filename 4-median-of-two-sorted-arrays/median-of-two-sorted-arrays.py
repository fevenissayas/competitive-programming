class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 = sorted(nums1 + nums2)
        if len (nums1) % 2 == 1:
            return float(nums1[len(nums1) // 2])
        else:
            mid1 = float(nums1[len(nums1) // 2 - 1])
            mid2 = float(nums1[len(nums1) // 2])
            
            return (mid1 + mid2) / 2        