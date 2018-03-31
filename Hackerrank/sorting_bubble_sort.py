""" Sorting: Bubble Sort
author : Woongwon Lee
problem : https://www.hackerrank.com/challenges/ctci-bubble-sort/problem
output :
You must print the following three lines of output:
Array is sorted in numSwaps swaps., where numSwaps is the number of swaps that took place.
First Element: firstElement, where firstElement is the first element in the sorted array.
Last Element: lastElement, where lastElement is the last element in the sorted array.
"""

import copy

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

count = 0
sorted_a = copy.deepcopy(a)
for i in range(n-1):
    for j in range(n-1):
        if sorted_a[j + 1] < sorted_a[j]:
            count += 1
            temp = copy.deepcopy(sorted_a[j])
            sorted_a[j] = sorted_a[j + 1]
            sorted_a[j + 1] = temp

print("Array is sorted in {:} swaps.".format(count))
print("First Element:", sorted_a[0])
print("Last Element:", sorted_a[-1])