# Problem: C - Compare T-Shirt Sizes - https://codeforces.com/gym/585107/problem/C

n = int(input())

for _ in range(n):
    a, b = map(str, input().split())
    if a[-1] > b[-1]:
        print('<')
    elif a[-1] < b[-1]:
        print('>')
    elif a == b:
        print ('=')
    elif a[-1] == b[-1] == 'S':
        if len(a) > len(b):
            print ('<')
        else:
            print('>')
    elif a[-1] == b[-1] == 'L':
        if len(a) > len(b):
            print('>')
        else:
            print('<')