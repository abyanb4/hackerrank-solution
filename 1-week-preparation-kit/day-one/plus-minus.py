import math
import os
import random
import re
import sys

def plusMinus(arr):
    # Write your code here
    many_positive = 0
    many_negative = 0
    many_zero = 0
    
    for i in range(0, len(arr)):
        if arr[i] < 0:
            many_negative += 1
            continue
        if arr[i] == 0:
            many_zero += 1
            continue
        if arr[i] > 0:
            many_positive += 1
            continue
    
    positive_ratio = round(many_positive/len(arr), 6)
    negative_ratio = round(many_negative/len(arr), 6)
    zero_ration = round(many_zero/len(arr), 6)
    
    print(positive_ratio)
    print(negative_ratio)
    print(zero_ration)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

"""
Sample input:
6              
-4 3 -9 0 4 1
"""
