class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        count = 0
        snum = str(num)

        for i in range(len(snum)-k + 1):
            val = int(snum[i:i+k])
            if val != 0 and num % val == 0:
                    count += 1
        return count