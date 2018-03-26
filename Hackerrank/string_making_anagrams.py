""" strings : making anagrams
author : Woongwon Lee
problem : https://www.hackerrank.com/challenges/ctci-making-anagrams/problem
output : Print a single integer denoting the number of characters you must
delete to make the two strings anagrams of each other.
"""

import copy


def number_needed(a, b):
    a_list = list(a)
    b_list = list(b)

    a_list_copy = copy.deepcopy(a_list)
    for a in a_list:
        if a in b_list:
            a_list_copy.remove(a)
            b_list.remove(a)

    return len(a_list_copy) + len(b_list)


a = input().strip()
b = input().strip()

print(number_needed(a, b))