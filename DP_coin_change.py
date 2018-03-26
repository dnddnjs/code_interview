'''
author : Woongwon Lee
Problem : https://www.hackerrank.com/challenges/ctci-coin-change/problem
'''


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