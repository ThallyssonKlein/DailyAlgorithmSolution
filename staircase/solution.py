#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    counter = 1
    while counter <= n:
        v = n - counter
        
        spaces = ' ' * (v)
        hashtags = '#' * (n - v)
        print(spaces + hashtags)
        counter += 1
if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
