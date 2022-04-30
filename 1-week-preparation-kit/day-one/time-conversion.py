import math
import os
import random
import re
import sys


def timeConversion(s):
    # Write your code here
    if s[-2:] == "PM" and s[:2] == "12":
        return(str(s[:-2]))
    elif s[-2:] == "PM":
        return(str(str((int(s[:2]) + 12)) + str(s[2:-2])))
    elif s[-2:] == "AM" and s[:2] == "12":
        return(str("00" + str(s[2:-2])))
    else:
        return(str(s[:-2]))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()

"""
Sample input
07:05:45PM
"""
