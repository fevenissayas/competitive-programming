# Problem: Books - https://codeforces.com/contest/279/problem/B

n, k = map(int, input().split())
arr = list(map(int, input().split()))

count = 0
summ = 0
left = 0
for right in range(n):
    summ += arr[right]
    while summ > k:
        summ -= arr[left]
        left += 1
    
    count = max(count, right-left+1)

print(count)