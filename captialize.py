#!/bin/python3

import math
import os
import random
import re
import sys
import string
# Complete the solve function below.
def solve(s):
    
    #t=str.title(map(title(),string.capwords(s)))

    t=" ".join(i.capitalize() for i in s)
    
    return(t)

if __name__ == '__main__':
  #  fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input().split()

    result = solve(s)

    """fptr.write(result + '\n')

    fptr.close()"""

    print(result)
