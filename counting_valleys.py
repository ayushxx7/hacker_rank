#!/bin/python3

import os

# We just need to calculate the number of valleys, so we are going to count the number of times we come 'Up' to sea level. 
def countingValleys(n, s):
    lvl = 0
    num_valleys = 0
    for step in s:
        print(step)
        if step == 'U':
            lvl += 1
            if lvl == 0:
                num_valleys += 1
        else:
            lvl -= 1 
    return num_valleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
