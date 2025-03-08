# Problem: F - Covered Points Count - https://codeforces.com/gym/589822/problem/F

t = int(input())

from collections import defaultdict
prefix = defaultdict(int)
for _ in range(t):
    ranges = list(map(int, input().split()))
    prefix[ranges[0]] += 1
    prefix[ranges[1] + 1] -= 1

key = sorted(prefix.keys())

ans = defaultdict(int)
running_sum = 0

for i in range(len(key) - 1):
    running_sum += prefix[key[i]]
    ans[running_sum] += (key[i+1] - key[i])

res = []
for i in range(1, t+1):
    res.append(ans[i] if i in ans else 0)

print(*res)
