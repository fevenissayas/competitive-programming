# Problem: Sort Characters By Frequency - https://leetcode.com/problems/sort-characters-by-frequency/description/

class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        for elem in count:
            sorted_ch = sorted(count.items(), key=lambda x: x[1], reverse=True)

        return ''.join([char[0]*char[1] for char in sorted_ch])