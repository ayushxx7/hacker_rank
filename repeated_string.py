#!/bin/python3
import os
# Complete the repeatedString function below.
def repeatedString(s, n):
    # string_x50 = s*n
    # index = 0
    # count = 0

    count = s.count('a')*(n//len(s)) + s[:n % len(s)].count('a')
    #### the logic lie in the simple fact that the string is supposed to be repeated, however it may not be a full repeatition everytime. 
    # meaning it could be a full repeatition or a partial one at the last section. 
    # so what we do is 
    # fist count the number of a's in a single string
    # then multiply this count by the floor of length of the string divided by the number n (number of letters until the string is repeated basically)
    # this gives us a base count for the wholly repeated portion of the string
    # now, if there lies a partial string, 
    # we generate the partial string like s[:n % len(s)] -> 
    # so that becomes remainder, 1000/5 = 20 + 0 vs 1000/3 = 333 + [1] <= colon receives this value. 
    # s[:1] means string s from 0 to 1 characters. 
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
