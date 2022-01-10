# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 23:26:45 2022

@author: Yashu
"""

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    #code here 
    mini=scores[0]
    maxi=scores[0]
    min_rec= 0
    max_rec=0
    for i in range(1,len(scores)):
        if(mini>scores[i]):
            mini=scores[i]
            min_rec=min_rec+1
        if(maxi<scores[i]):
            maxi=scores[i]
            max_rec=max_rec+1
    return max_rec,min_rec
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
