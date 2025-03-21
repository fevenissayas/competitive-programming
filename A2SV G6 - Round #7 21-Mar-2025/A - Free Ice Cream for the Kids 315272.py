# Problem: A - Free Ice Cream for the Kids - https://codeforces.com/gym/596141/problem/A

n , m = map(int, input().split())
q = []
for _ in range(n):
    q.append(list(input().split()))

ans = m
count = 0
for e, num in q:
    if e == "+":
        ans += int(num)
    else:
        if ans < int(num):
            count += 1
        else:
            ans -= int(num)

print(ans, count)
