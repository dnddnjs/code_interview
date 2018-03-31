""" Hash Tables: Ice Cream Parlor
author : Woongwon Lee
problem : https://www.hackerrank.com/challenges/ctci-ice-cream-parlor/problem
output : Print two space-separated integers denoting the respective ID numbers
for the two distinct flavors they choose to purchase, where the smaller ID is
printed first and the larger ID is printed second. Recall that each ice cream
flavor has a unique ID number in the inclusive range from 1 to flavors.
"""


def solve(arr, money):
    map = {}
    for id, cost in enumerate(arr):
        if cost in map:
            print(map[cost], id + 1)
        else:
            map[money - cost] = id + 1


if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        money = int(input().strip())
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        solve(arr, money)