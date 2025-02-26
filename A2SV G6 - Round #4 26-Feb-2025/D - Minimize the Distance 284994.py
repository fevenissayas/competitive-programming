# Problem: D - Minimize the Distance - https://codeforces.com/gym/590053/problem/D

n = int(input())
lst = list(map(int, input().split()))
lst.sort()

if n%2:
    print (lst[n//2])
else:
    print(lst[n//2-1])