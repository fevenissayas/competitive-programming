# Problem: B - Fix the Forecast! - https://codeforces.com/gym/591928/problem/B

n = int(input())
for _ in range(n):
    m, k = map(int, input().split())
    a = list(map(int, input().split()))

    for i, val in enumerate(a):
        a[i] = [val, i]

    a = sorted(a)
    b = sorted(list(map(int, input().split())))
    ans = [0] * m

    for i, w in enumerate(a):
        ans[w[1]] = b[i]

    print(*ans)