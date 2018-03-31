""" Time Complexity: Primality
author : Woongwon Lee
problem : https://www.hackerrank.com/challenges/ctci-bfs-shortest-reach/problem
output : For each integer, print whether n is Prime or Not prime on a new line.
"""

from math import sqrt


def check_primality(num):
    if num <= 1:
        return "Not prime"
    elif num <= 3:
        return "Prime"
    elif (num % 2 == 0) or (num % 3 == 0):
        return "Not prime"
    
    k = 1
    while 6 * k + 1 <= int(sqrt(num) + 2):
        if (num % (6 * k - 1) == 0) or (num % (6 * k + 1) == 0):
            return "Not prime"
        k += 1
    return "Prime"


p = int(input().strip())
for a0 in range(p):
    n = int(input().strip())
    out = check_primality(n)
    print(out)
