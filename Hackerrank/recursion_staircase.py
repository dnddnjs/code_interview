""" Recursion: Davis' Staircase
author : Woongwon Lee
problem : https://www.hackerrank.com/challenges/ctci-recursive-staircase/problem

Davis has s staircases in his house and he likes to climb each staircase 1, 2,
or 3 steps at a time. Being a very precocious child, he wonders how many ways
there are to reach the top of the staircase.

Given the respective heights for each of the s staircases in his house, find
and print the number of ways he can climb each staircase on a new line.

output : For each staircase, print the number of ways Davis can climb it in a new line.
"""

seen = {1: 1, 2: 2, 3: 4}


def count_ways(n):
    if n <= 3:
        return seen[n]

    if n in seen:
        return seen[n]

    combine = count_ways(n - 3) + count_ways(n - 2) + count_ways(n - 1)
    seen[n] = combine
    return combine


s = int(input().strip())
for a0 in range(s):
    n = int(input().strip())
    num_ways = count_ways(n)
    print(num_ways)
