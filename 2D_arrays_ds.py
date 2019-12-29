#!/bin/python3
import os

# Complete the hourglassSum function below.
### This is the first problem that I could solve completely on my own. Although it isn't that hard, it still felt good to not take a look at the hints for once. 
# The logic is simple,
# first you think of hourglass formation constraint. 
# based on that you will only loop i,j -> 0 to 3 as going beyond these values doesn't form hourglass. 
# next you want to add the sum of the hourglass values, which is basically a game of just indexing the right elements. 
# i.e. the elements that form the hour glass. the indexing is self explanatory in the code itself. 
def hourglassSum(arr):

    max_sum = -100 # for corner case, we should not keep this variable's value as 0, as max sum can be negative as well. 
    for i in range(4):
        for j in range(4):
            curr_sum = arr[i][j] + arr[i][j+1] + \
            arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + \
            arr[i+2][j+1] + arr[i+2][j+2]

            print(curr_sum)

            if max_sum < curr_sum:
                max_sum = curr_sum
    return max_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
