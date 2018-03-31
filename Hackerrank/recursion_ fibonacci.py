""" Recursion: Fibonacci Numbers
author : Woongwon Lee
problem : https://www.hackerrank.com/challenges/ctci-fibonacci-numbers/problem
output : Locked stub code in the editor prints the value of fibonacci(n)
returned by the fibonacci function.
"""

def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

n = int(input())
print(fibonacci(n))
