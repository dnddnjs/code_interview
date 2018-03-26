""" stacks : balanced brackets
author : Woongwon Lee
problem : https://www.hackerrank.com/challenges/ctci-balanced-brackets/problem
output : For each string, print whether or not the string of brackets is
balanced on a new line. If the brackets are balanced, print YES;
otherwise, print NO.
"""

def is_matched(expression):
    if len(expression) % 2 != 0:
        return False

    lists = []
    for char in expression:
        if char in ['{', '[', '(']:
            lists.append(char)
        else:
            if len(lists) > 0:
                if char == '}':
                    if lists.pop() != '{':
                        return False
                if char == ')':
                    if lists.pop() != '(':
                        return False
                if char == ']':
                    if lists.pop() != '[':
                        return False
            else:
                return False

    if len(lists) > 0:
        return False
    else:
        return True


t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")