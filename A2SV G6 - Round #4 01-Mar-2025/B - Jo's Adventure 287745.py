# Problem: B - Jo's Adventure - https://codeforces.com/gym/590053/problem/B

n, m = map(int, input().split())
lst = list(map(int, input().split()))
px = [0] * n
sx = [0] * n

for i in range(1, n):
    maxx = max(0, lst[i - 1] - lst[i])
    px[i] = px[i - 1] + maxx
    
for i in range(n - 2, -1, -1):
    maxx = max(0, lst[i + 1] - lst[i])
    sx[i] = sx[i + 1] + maxx
     

for _ in range(m):
    a, b = map(int, input().split())
    
    if b <= a:
        print(sx[b - 1] - sx[a - 1])
    else:
        print(px[b - 1] - px[a - 1])
