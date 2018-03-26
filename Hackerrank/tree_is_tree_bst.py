""" trees : Is this a binary search tree?
author : Woongwon Lee
problem : https://www.hackerrank.com/challenges/ctci-is-binary-search-tree/problem
output : You are not responsible for printing any output to stdout.
Your function must return true if the tree is a binary search tree;
otherwise, it must return false. Hidden code stubs will print this result
 as a Yes or No answer on a new line.
"""


def checkBST(root):
    if root is None:
        return True

    stack = [(float('-inf'), root, float('+inf'))]
    while stack:
        mind, node, maxd = stack.pop()
        if not (mind < node.data < maxd):
            return False
        if node.left is not None:
            stack.append((mind, node.left, node.data))
        if node.right is not None:
            stack.append((node.data, node.right, maxd))
    return True
