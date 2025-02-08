# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses/

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        count_win = Counter()
        count_lose = Counter()
        ans = []

        for elem in matches:
            count_win[elem[0]] += 1
            count_lose[elem[1]] += 1

        for num in count_lose:
            if count_lose[num] == 1:
                ans.append(num)
            if num in count_win:
                del(count_win[num])

        return [list(sorted(count_win.keys())), sorted(ans)]