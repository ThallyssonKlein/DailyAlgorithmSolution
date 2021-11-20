#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApples(s, t, a, apples):
    toReturn = []
    for apple in apples:
        if apple+a >= s and apple+a <= t:
            toReturn.append(apple)
    return len(toReturn)

def countOranges(s, t, b, oranges):
    toReturn = []
    for orange in oranges:
        if orange+b >= s and orange+b <= t:
            toReturn.append(orange)
    return len(toReturn)

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    print(countApples(s, t, a, apples))
    print(countOranges(s, t, b, oranges))

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
