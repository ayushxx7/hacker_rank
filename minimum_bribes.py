#!/bin/python3
import os

# Complete the minimumBribes function below.
def minimumBribes(q):
    
    bribes = 0
    q = [p-1 for p in q] ### for understand the indexing better. 
    # atq value is from 1 to n, while loop runs from 0 to n-1. 

    for i,p in enumerate(q): 
        # print('i:',i,'p',p)
        if p > i + 2: # condition mentioned that no person can bribe more than 2 people in front of them, 
            print('Too chaotic')
            return
        else:
            for j in range(max(p-1,0),i): #  subtracting value by 2->iterating upto iTH value.  
                # print('j:',j,'q[j]:',q[j])
                if q[j] > p: # to calculate number of times a person has bribed a person (now) behind them
                    bribes += 1
    
    print(bribes)
    # i = 1
    # n = len(q)
    # bribes = 0

    
    # for i in range(1,n+1):
    #     if q[i-1] > i + 2: 
    #         # print(q[i-1],i+2)
    #         print('Too chaotic!')
    #         return
    #     else:
    #         for j in range(max(0,q[i]-2),i):
    #             # print('j:',j)
    #             if q[j] < q[i-1]:
    #                 bribes += 1
    
    # print(bribes)
    # return


    # while i < n:
    #     if q[i-1] == i:
    #         i += 1
    #     elif q[i-1] <= i + 2:
    #         if q[i-1] == i+2: 
    #             print('==2')
    #             bribes += 1
    #             i += 2
    #         else:
    #             print('==1')
    #             bribes += 1
    #             i += 1
    #     else:
    #         print('Too chaotic')
    #         return
    # print(bribes)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
