#!/bin/python3

import math
import os
import random
import re
import sys

def balancedSums(arr):
    total = sum(arr)
    left_sum = 0

    for num in arr:
        right_sum = total - left_sum - num

        if left_sum == right_sum:
            return "YES"

        left_sum += num

    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()