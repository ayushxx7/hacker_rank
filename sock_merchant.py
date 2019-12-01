'''
Question Link: https://www.hackerrank.com/challenges/sock-merchant/
'''

### SUBMITTED SOLUTION: (ALL CASES PASSED)
#!/bin/python3

import os # not required for local copy.
from collections import Counter

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    '''
    Counter is a neat function from collections library. 
    -> converts list to dictionary {key:value} == {value_in_ar:count_of_value_in_ar}
    -> .values is used to extract the value list from any dictionary's key:value. 
    '''
    pair_count = 0
    for values in Counter(ar).values():
        pair_count += values//2
    return pair_count

## local example
print(sockMerchant(6,[1,1,2,2,3,3]))
##
    ### ATTEMP 1: 3 cases passed
    # pair_count = 0
    
    # for i in range(n):
    #     print('i:',i)
    #     for j in range(1,n):
    #         print('j:',j)
    #         try:
    #             ar[i]
    #             if ar[j] == ar[i]:
    #                 ar.pop(i)
    #                 ar.pop(j)
    #                 pair_count += 1
    #                 print('PAIR ++')
    #                 print('Array: ',ar)
    #                 break
    #         except:
    #             i = 0
    #             j = 1

    # return pair_count
    # pass

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input())

#     ar = list(map(int, input().rstrip().split()))

#     result = sockMerchant(n, ar)

#     fptr.write(str(result) + '\n')

#     fptr.close()
