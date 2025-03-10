# Problem: F - Binary Substrings with Exactly k Ones - https://codeforces.com/gym/588468/problem/F

k = int(input())
nums = list(map(int, list(input())))

from collections import defaultdict
count = defaultdict(int)
ans = 0
summ = 0
count[0] = 1

for val in nums:
    summ += val
    ans += count[summ-k]
    count[summ] += 1 

print(ans)