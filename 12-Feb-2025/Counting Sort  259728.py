# Problem: Counting Sort  - https://www.hackerrank.com/challenges/countingsort1/problem

def countingSort(arr):
    # Write your code here
    lst = [0]*(100)
    for elem in arr:
        lst[elem] += 1
        
    return lst