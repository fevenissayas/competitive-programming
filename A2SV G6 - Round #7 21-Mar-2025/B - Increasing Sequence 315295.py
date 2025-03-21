# Problem: B - Increasing Sequence - https://codeforces.com/gym/596141/problem/B

t = int(input())

def func():
    n = int(input())
    nums = list(map(int, input().split()))
    ans = []

    for num in nums:
        if not ans:
            if num > 1:
                ans.append(1)
            else:
                ans.append(num + 1)
        else:
            if num > ans[-1]:
                if num - ans[-1] == 1:
                    ans.append(num + 1)
                else:
                    ans.append(ans[-1] + 1)
            else:
                ans.append(ans[-1] + 1)
    return ans[-1]
    
for _ in range(t):
    print(func())
