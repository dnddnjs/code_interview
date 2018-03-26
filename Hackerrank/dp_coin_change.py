""" dynamic programming : coin change
author : Woongwon Lee
problem : https://www.hackerrank.com/challenges/ctci-coin-change/problem
output : Print a single integer denoting the number of ways we can make change
for  dollars using an infinite supply of our  types of coins.
"""

def make_change(coins, n):
    lookup = [1] + [0] * n
    for coin in coins:
        for i in range(n+1-coin):
            lookup[i+coin] += lookup[i]
    return lookup[n]

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
coins = [int(coins_temp) for coins_temp in input().strip().split(' ')]
print(make_change(coins, n))