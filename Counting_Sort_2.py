#!/bin/python3

import os
import sys

def countingSort(arr):
    count = [0] * 100

    for num in arr:
        count[num] += 1

    result = []

    for i in range(100):
        result += [i] * count[i]

    return result


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().split()))

    result = countingSort(arr)

    print(*result)