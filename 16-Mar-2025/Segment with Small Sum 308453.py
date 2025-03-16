# Problem: Segment with Small Sum - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/A

n, s = map(int, input().split())
arr = list(map(int, input().split()))

def segment_sum (arr, n, s):
    left = 0
    summ = 0
    max_length = 0

    for right in range (n):
        summ += arr[right]
        while summ > s:
            summ -= arr[left]
            left += 1

        max_length = max(max_length, right-left+1)

    return max_length

print(segment_sum(arr, n, s))