# Problem: Sum - https://codeforces.com/contest/1742/problem/A

n = int(input())

for _ in range (n):
    lst = sorted(list(map(int, input().split())))
    if lst[0] + lst [1] == lst[-1]:
        print('YES')
    else:
        print('NO')