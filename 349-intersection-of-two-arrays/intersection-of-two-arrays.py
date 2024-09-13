class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen1 = set(nums1)
        seen2 = set(nums2)
        lst = []

        for i in seen1:
            if i in seen2:
                lst.append(i)
        return lst