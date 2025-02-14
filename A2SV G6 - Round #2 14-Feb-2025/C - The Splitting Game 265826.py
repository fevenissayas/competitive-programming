# Problem: C - The Splitting Game - https://codeforces.com/gym/586960/problem/C

n = int(input())

from collections import Counter
for _ in range(n):
    a = int(input())
    s = input()

    count1 = Counter()
    count2 = Counter(s)
    
    summ = len(count2)
    for i in range(a):
        count1[s[i]] += 1
        count2[s[i]] -= 1

        if count2[s[i]] == 0:
            del(count2[s[i]])
        summ = max(summ, len(count1) + len(count2))
    
    print(summ)