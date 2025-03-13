# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        ans = 0
        for key, val in count.items():
            leng = key + 1
            val = ceil(val/leng)
            ans += val * leng
                
        return ans