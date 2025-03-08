# Problem: D - Socialism - https://codeforces.com/gym/589822/problem/D

t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    a = sorted(map(int, input().split()))
    riches = 0
    money = 0
 
 
    for i in range(n):
        if a[i] >= x:
            riches += 1
            money += a[i] - x
        
    for i in range(n - 1,-1,-1):
        if a[i] < x:
            money -= (x - a[i])
            if money < 0:
                break
            else:
                riches += 1
 
    print(riches)