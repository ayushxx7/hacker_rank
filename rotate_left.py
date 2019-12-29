#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
# def rotate(a):
#     ini = a[0]
#     for i in range(1,len(a)):
#         a[i-1] = a[i]
#     n = len(a)
#     a[n-1] = ini
def rotLeft(a, d):
    # b = a
    # n = len(a)
    # print(b,a)
    # for i in range(n):
    #     new_i = (i+d)%n
    #     print(i,new_i)
    #     print(b[i],a[new_i])
        # print(new_i)
        # b[i] = a[new_i]
        # print(b[i])
    # i = 0
    # n = len(a)
    # while i < n:
    #     new_i = (i + (n-d-1))%n
    #     a[new_i] = a[i+1]
    #     i += 1
    # b = a
    # for i in range(len(a)-1):
    #     new_i = (i + (len(a)-d))%len(a)
    #     a[new_i] = a[i]
    return a[d:] + a[:d]  ### the easiest way out for this question is to use list slicing. 
    ## I however do not understand why this approach above is not working. 
    # new_i always returns value 5 for some reason. 

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    print(result)

    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
