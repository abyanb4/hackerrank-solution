import math
import os
import random
import re
import sys


def miniMaxSum(arr):
    # Write your code here
    sum_exception = 0
    sum_result = []
    max_sum = 0
    min_sum = 0
    
    for i in range(0, len(arr)):
        temp_sum = 0
        for x in range(0, len(arr)):
            if x == i:
                continue
            else:
                temp_sum += arr[x]
                
        if temp_sum > max_sum:
            max_sum = temp_sum
        if temp_sum < min_sum or i == 0:
            min_sum = temp_sum
            
    print("{} {}".format(min_sum,  max_sum))
            

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

"""
Sample input
1 2 3 4 5
"""
