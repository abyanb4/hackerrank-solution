import os

"""Find the median"""


def findMedian(arr):
    arr.sort()
    len_arr = len(arr)//2
    
    return arr[len_arr]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)

    fptr.write(str(result) + '\n')

    fptr.close()