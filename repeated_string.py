#!/bin/python3
import os
# Complete the repeatedString function below.
def repeatedString(s, n):
    # string_x50 = s*n
    # index = 0
    # count = 0

    count = s.count('a')*(n//len(s)) + s[:n % len(s)].count('a')

    # while index < len(s):
    #     if s[index] == 'a':
    #         count += 1
    #     index += 1
    
    # count = count * round(n/len(s))
    
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
