# Problem: Minimum Index Sum of Two Lists - https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        min_sum = float('inf')
        lst = []

        for i, val1 in enumerate (list1):
            d1[val1] = i
        for i, val2 in enumerate (list2):
            d2[val2] = i

        for items in d1:
            if items in d2:
                if d1[items] + d2[items] < min_sum:
                    min_sum = d1[items] + d2[items]
                    lst = [items]
                elif d1[items] + d2[items] == min_sum:
                    lst.append(items)

        return lst