# Problem: Love Story - https://codeforces.com/contest/1829/problem/A

n = int(input())
s = "codeforces"

for _ in range(n):
    inp = input()
    count = 0
    for i in range(10):
        if inp[i] != s[i]:
            count += 1
    
    print (count)