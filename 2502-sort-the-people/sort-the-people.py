class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        while True:
            flag = False
            for j in range(len(names) - 1):
                if heights[j] < heights[j + 1]:
                    heights[j], heights[j + 1] = heights[j + 1], heights[j]
                    names[j], names[j + 1] = names[j + 1], names[j]
                    flag = True
            if not flag:
                break
        return names