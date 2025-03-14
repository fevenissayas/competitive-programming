# Problem: Insertion Sort - https://www.hackerrank.com/challenges/insertionsort1/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    j = n - 2
    val = arr[-1]
    while j >= 0 and arr[j] > val:
        arr[j+1] = arr [j]
        j -= 1
        print(' '.join(map(str, arr)))
    arr [j+1] = val
    print(' '.join(map(str, arr)))    
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
