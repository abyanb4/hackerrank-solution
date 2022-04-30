import math
import os
import random
import re
import sys

def lonelyinteger(a):
    # Write your code here
    d = {}
    
    for item in a:
        if item not in d:
            d[item] = 1
        else:
            d[item] = 2
            
    for key, value in d.items():
        if value == 1:
            return key

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
