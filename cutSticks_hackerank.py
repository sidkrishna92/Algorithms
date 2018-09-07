import math
import os
import random
import re
import sys
import numpy as np

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    counts = [len(arr)]

    while len(arr) > 1:
        new_arr = []
        min_val = min(arr)

        new_arr = [val - min_val for val in arr if val != min_val]
        if new_arr!=[]:
            count = len(new_arr)
            counts.append(count)
        arr = new_arr

    return counts




if __name__ == '__main__':
    # n = int(input())
    n = 8
    # arr = list(map(int, input().rstrip().split()))
    arr = [8, 8, 14, 10, 3, 5, 14, 12]
    result = cutTheSticks(arr)
    print(result)