""" queue : a tale of two stacks
author : Woongwon Lee
problem : https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks/problem
output : For each query of type 3, print the value of the element at the front
of the queue on a new line.
"""


class MyQueue(object):
    def __init__(self):
        self.queue = []

    def peek(self):
        return self.queue[0]

    def pop(self):
        pop_value = self.queue[0]
        if len(self.queue) > 1:
            self.queue = self.queue[1:]
        else:
            self.queue = []
        return pop_value

    def put(self, value):
        self.queue.append(value)


queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())