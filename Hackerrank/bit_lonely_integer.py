""" Bit Manipulation: Lonely Integer
author : Woongwon Lee
problem : https://www.hackerrank.com/challenges/ctci-lonely-integer/problem
output : Print the unique number that occurs only once in  on a new line.
"""

def lonely_integer(a):
    numbers = list(set(a))
    numbers_dict = {}
    for i in range(len(numbers)):
        numbers_dict[numbers[i]] = 0

    for i in range(len(a)):
        numbers_dict[a[i]] += 1

    onlyone_index = list(numbers_dict.values()).index(1)
    onlyone_number = list(numbers_dict.keys())[onlyone_index]
    return onlyone_number


n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
print(lonely_integer(a))