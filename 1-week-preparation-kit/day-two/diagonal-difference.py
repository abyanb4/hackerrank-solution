import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    # Write your code here
    sum_first_diagonal = 0
    sum_second_diagonal = 0
    
    len_row = len(arr[0]) - 1
    
    for i in range(0, len(arr[0])):
        sum_first_diagonal += arr[i][i]
        sum_second_diagonal += arr[i][len_row]
        
        len_row -= 1
        
    return abs(sum_first_diagonal - sum_second_diagonal)
            
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

"""
Sample input

3
11 2 4
4 5 6
10 8 -12

"""
