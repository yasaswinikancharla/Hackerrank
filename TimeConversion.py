# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 22:15:52 2022

@author: Yashu
"""

#!/bin/python3


import math
import os
import random
import re
import sys


#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    a=s[-2:]
    if(a=="PM"):
        x=s[:-2].split(":")
        if(int(x[0])==12):
            x[0]=12
        else:
            x[0]=int(x[0])+12
        s=str(x[0])+":"+x[1]+":"+x[2]
    else:
        x=s[:-2].split(":")
        if(int(x[0])==12):
            x[0]="00"
        s=x[0]+":"+x[1]+":"+x[2]
    return s
    
if __name__ == '__main__':
    

    s = input()

    result = timeConversion(s)

    print(result)
