""" linked lists : detect a cycle
author : Woongwon Lee
problem : https://www.hackerrank.com/challenges/ctci-linked-list-cycle/problem
output : If the list contains a cycle, your function must return true.
If the list does not contain a cycle, it must return false.
The binary integer corresponding to the boolean value returned by your
function is printed to stdout by our hidden code checker.
"""
"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 

    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    curr = head
    seen = set()
    while curr:
        if curr in seen:
            return True
        seen.add(curr)
        curr = curr.next
    return False