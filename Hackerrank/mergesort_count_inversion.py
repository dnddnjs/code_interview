""" Merge Sort: Counting Inversions
author : Woongwon Lee
problem : https://www.hackerrank.com/challenges/ctci-ice-cream-parlor/problem
output : For each of the  datasets, print the number of inversions that must
be swapped to sort the dataset on a new line.
"""


def countInversions(arr):
    if len(arr) <= 1:
        return arr, 0

    left_arr, left_inv = countInversions(arr[:int(len(arr) / 2)])
    right_arr, right_inv = countInversions(arr[int(len(arr) / 2):])

    result = []
    i, j, inversion = 0, 0, 0
    len_left = len(left_arr)
    len_right = len(right_arr)
    while i < len_left and j < len_right:
        if left_arr[i] <= right_arr[j]:
            result.append(left_arr[i])
            i += 1
        else:
            result.append(right_arr[j])
            inversion += len_left - i
            j += 1

    result += left_arr[i:]
    result += right_arr[j:] 
    return result, inversion + right_inv + left_inv


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    _, count = countInversions(arr)
    print(count)
