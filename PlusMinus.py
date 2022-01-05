
"""
Created on Tue Jan  4 13:13:22 2022

@author: Yashu
"""

#!/bin/python3


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    n=len(arr)
    pos_cou=0
    neg_cou=0
    zero_cou=0
    for i in arr:
        if(i>0):
            pos_cou=pos_cou+1
        elif(i==0):
            zero_cou=zero_cou+1
        elif(i<0):
            neg_cou=neg_cou+1
    print((pos_cou/n),end="\n")
    print((neg_cou/n),end="\n")
    print((zero_cou/n),end="\n")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
