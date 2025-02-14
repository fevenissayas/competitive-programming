# Problem: Longest k-Good Segment - https://codeforces.com/problemset/problem/616/D

n, k = map(int, input().split())
arr = list(map(int, input().split()))

from collections import Counter
count = Counter()
max_len = 0
left = 0
for right in range(n):
    count[arr[right]] += 1
    while len(count) > k:
        count[arr[left]] -= 1
        if count[arr[left]] == 0:
            del count[arr[left]]
        left += 1
    
    if max_len < right-left+1:
        ans = [left+1, right+1]
        max_len = right-left+1

print(*ans)