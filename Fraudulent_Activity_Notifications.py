#!/bin/python3

import os
import sys

def activityNotifications(expenditure, d):
    count = [0] * 201

    for i in range(d):
        count[expenditure[i]] += 1

    notifications = 0

    for i in range(d, len(expenditure)):

        total = 0
        median_sum = 0
        first = (d + 1) // 2
        second = (d + 2) // 2

        for j in range(201):
            total += count[j]

            if total >= first and median_sum == 0:
                median_sum += j

            if total >= second:
                median_sum += j
                break

        if expenditure[i] >= median_sum:
            notifications += 1

        count[expenditure[i - d]] -= 1
        count[expenditure[i]] += 1

    return notifications


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])
    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()