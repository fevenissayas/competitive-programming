# Problem: Pass the Pillow - https://leetcode.com/problems/pass-the-pillow/description/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        res = 1
        direction = 1
        for i in range(time):
            res += direction
            if res == 1:
                direction = 1
            elif res == n:
                direction = -1

        return res