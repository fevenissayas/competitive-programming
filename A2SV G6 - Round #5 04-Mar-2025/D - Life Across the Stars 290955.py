# Problem: D - Life Across the Stars - https://codeforces.com/gym/591928/problem/D


from collections import defaultdict
dic = defaultdict(int)

n = int(input())
for _ in range(n):
    b, d = map(int, input().split())
    dic[b] += 1
    dic[d] -= 1

k = sorted(dic.keys())
prefix = []
val = 0
for elem in k:
    val += dic[elem]
    prefix.append(val)

A = k[0]
B = prefix[0]

for i in range(1, len(prefix)):
    if prefix[i] > B:
        A = k[i]
        B = prefix[i]

print(A, B)
