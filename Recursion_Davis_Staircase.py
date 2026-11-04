#!/bin/python3

import math
import os
import random
import re
import sys
from functools import lru_cache

#
# Complete the 'stepPerms' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

MOD = 10000000007

@lru_cache(maxsize=None)
def stepPerms(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    return (stepPerms(n - 1) + stepPerms(n - 2) + stepPerms(n - 3)) % MOD

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input().strip())

    for s_itr in range(s):
        n = int(input().strip())

        res = stepPerms(n)

        fptr.write(str(res) + '\n')

    fptr.close()