""" arrays : left rotation
author : Woongwon Lee
problem : https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem
output : Print a single line of n space-separated integers denoting the final
state of the array after performing d left rotations.
"""

def array_left_rotation(a, n, k):
    new_array = []
    for i in range(n):
        new_array.append(i)

    for i in range(n):
        if k > i:
            new_array[n + i - k] = a[i]
        else:
            new_array[i - k] = a[i]

    return new_array


n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')
