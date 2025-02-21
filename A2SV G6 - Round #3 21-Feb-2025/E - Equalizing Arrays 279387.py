# Problem: E - Equalizing Arrays - https://codeforces.com/gym/588468/problem/E

n = int(input())
a1 = list(map(int, input().split()))
m = int(input())
b1 = list(map(int, input().split()))

from collections import Counter

def equalizing_arr(n, a1, m, b1):
    if sum(a1) != sum(b1):
        return -1
    
    i = j = 0
    count = 0
    s_a1 = 0
    s_b1 = 0    
    while i < n and j < m:
        s_a1 += a1[i]
        s_b1 += b1[j]
        
        while s_a1 != s_b1:
            if s_a1 >= s_b1:
                j += 1
                if j < m:
                    s_b1 += b1[j]
            else:
                i += 1
                if i < n:
                    s_a1 += a1[i]
        
        count += 1
        i += 1
        j += 1
        s_a1, s_b1 = 0, 0

    return count

print(equalizing_arr(n, a1, m, b1))