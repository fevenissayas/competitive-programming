# Problem: F - Array Transformation - https://codeforces.com/gym/586960/problem/F

from collections import defaultdict

t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    count = defaultdict(int)
    dic = defaultdict(int)
    for num in nums:
        count[num] += 1
        current_count = count[num]
        dic[current_count] += 1

    maxx = 0
    for key , val in dic.items():
        maxx = max(key * val , maxx)

    print(n - maxx)