#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
'''
The logic involves stealing code.
I do not understand it myself yet. 
The one key thing to reduce number of swaps is to check whether iTH element = i due to it be a consecutive list of integers. 
If it is not so, you would indeed have to swap so you increase the swap count by 1. 
You will store a temporary variable for swapping iTH element from arr. 
At the same time, you will intuitively know the position of the element at temporary variable's location in the array. 
'''
def minimumSwaps(arr):

    n = len(arr)
    temp_arr = [0]*(n+1)

    for pos,val in enumerate(arr):
        temp_arr[val] = pos
        pos+=1
    swap_count = 0

    for i in range(n):
        if arr[i]!= i+1:
            swap_count += 1
            t = arr[i]
            arr[i] = i+1
            arr[temp_arr[i+1]] = t
            temp_arr[t] = temp_arr[i+1]
    return swap_count
    # n = len(arr)
    # gap = n//2
    # swap_count = 0
    # while gap > 0:
    #     for i in range(gap,n):

    #         temp = arr[i]

    #         j = i
    #         while j>=gap and arr[j-gap]>temp:
    #             arr[j] = arr[j-gap]
    #             j-=gap
    #         arr[j] = temp
    #         swap_count += 1
    #     gap//=2
    # return swap_count
    # for gap in range(n/2,0,)
    # n = len(arr)
    # swap_count = 0

    # for i in range(n-1):
    #     min_idx = i
    #     j = i+1
    #     if j == arr[i]:
    #         continue
    #     for j in range(i+1,n):
    #         if arr[j] < arr[min_idx]:
    #             min_idx = j
    #     temp = arr[min_idx]
    #     arr[min_idx] = arr[i]
    #     arr[i] = temp
    #     swap_count += 1
    # print(arr)
    # return swap_count

    
    # for i in range(1,n):
    #     j = i-1
    #     key = arr[i]
    #     while j>=0 and arr[j]>key:
    #         arr[j+1] = arr[j]
    #         swap_count += 1
    #         j-=1
    #     arr[j+1] = key
    # print(arr)
    # return swap_count



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
