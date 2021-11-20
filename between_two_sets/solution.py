#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    print(a)
    print(b)
    
    finalSelecteds = []
    
    x = 1
    
    while x <= 100:
        xs = []
        correct = 0
        for number in a:
            if x % number == 0:
                correct += 1
        
        if correct == len(a):
            xs.append(x)
        
        correct = 0
        
        if len(xs) > 0:
            for number in b:
                if number % x == 0:
                    correct += 1
        
        if correct == len(b) and x in xs:
            finalSelecteds.append(x)
        
        x += 1
    
    return len(finalSelecteds)
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
