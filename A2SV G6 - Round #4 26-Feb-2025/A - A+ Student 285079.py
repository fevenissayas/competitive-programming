# Problem: A - A+ Student - https://codeforces.com/gym/590053/problem/A

n = int(input())

for _ in range(n):
    a,b,c = map(int, input().split())
    lst = []
    if a == b == c:
        lst = [1]*3

    else:
        lst.append(max(0, max(b,c)-a+1))
        lst.append(max(0, max(a,c)-b+1))
        lst.append(max(0, max(b,a)-c+1))
        
    print(*lst)