# Problem: E - From S To T - https://codeforces.com/gym/585107/problem/E

q = int(input())
for _ in range(q):
    s = input().strip()
    t = input().strip()
    p = input().strip()
    
    it = iter(t)
    if not all(c in it for c in s):
        print("NO")
        continue
    
    from collections import Counter
    cs, ct, cp = Counter(s), Counter(t), Counter(p)
    
    if all(cs[c] + cp[c] >= ct[c] for c in ct):
        print("YES")
    else:
        print("NO")