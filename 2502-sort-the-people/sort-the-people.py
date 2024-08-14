class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dic = dict(zip(heights,names))
        lst_h = sorted(heights, reverse=True)
        return (dic[h] for h in lst_h)