#!/bin/python3
import os
# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):

    index = 0
    step = -1
    size = len(c)

    while index < size:
        print(c[index])
        if index + 2 < size and c[index] == 0: ## the logic is simple, you are going to jump either 1 step or 2 step, based on if 2 step jump is leading to a 0(safe) or 1. 
            index = index + 1
        step += 1
        index += 1
    
    return step
    # step_count = -1
    # print(c)
    # for index,step in enumerate(c):
    #     print(c[index])
    #     if index+2 < len(c):
    #         if c[index+2] == 0:
    #             index = index+1
    #             step_count += 1
    #     else:
    #         step_count += 1
    # return step_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
