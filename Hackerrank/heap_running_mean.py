""" heaps : running mean
author : Woongwon Lee
problem : https://www.hackerrank.com/challenges/ctci-find-the-running-median/problem
output : After each new integer is added to the list, print the list's updated
median on a new line as a single double-precision number scaled to 1 decimal
place (i.e., 12.3 format).
"""
import bisect

n = int(input().strip())

list_i = []
a_i = 0
for a_i in range(n):
    a_t = int(input().strip())
    bisect.insort(list_i, a_t)
    if len(list_i) % 2 == 0:
        mid_left = len(list_i) // 2 - 1
        mid_right = len(list_i) // 2
        print('{:0.1f}'.format((list_i[mid_left] + list_i[mid_right]) / 2))
    else:
        mid = len(list_i) // 2
        print('{:0.1f}'.format(list_i[mid]))

