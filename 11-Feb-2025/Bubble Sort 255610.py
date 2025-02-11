# Problem: Bubble Sort - https://www.hackerrank.com/challenges/ctci-bubble-sort/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    count = 0
    while True:
        flag = False
        for i in range (n-1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                count += 1
                flag = True
                
        if flag == False:
            break
    print(f"""Array is sorted in {count} swaps.
First Element: {a[0]}
Last Element: {a[-1]}""")


if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
