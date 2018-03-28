""" bfs : shortest reach in a graph
author : Woongwon Lee
problem : https://www.hackerrank.com/challenges/ctci-bfs-shortest-reach/problem
output : For each of the q queries, print a single line of n-1 space-separated
integers denoting the shortest distances to each of the n-1 other nodes from
starting position s. These distances should be listed sequentially by node
number (i.e., 1, 2, 3,), but should not include node s. If some node is
unreachable from s, print -1 as the distance to that node.
"""

from collections import defaultdict
import queue


class Graph:
    def __init__(self, num_node):
        self.num_node = num_node
        self.edges = defaultdict(lambda: [])

    def connect(self, node1, node2):
        self.edges[node1].append(node2)
        self.edges[node2].append(node1)

    def find_all_distances(self, root):
        distances = [-1 for i in range(self.num_node)]
        unvisited = set([i for i in range(self.num_node)])
        q = queue.Queue()

        distances[root] = 0
        unvisited.remove(root)
        q.put(root)

        while not q.empty():
            node = q.get()
            children = self.edges[node]
            height = distances[node]

            for child in children:
                if child in unvisited:
                    distances[child] = height + 6
                    unvisited.remove(child)
                    q.put(child)

        # delete root index value from distances
        distances.pop(root)
        print(" ".join(map(str, distances)))


t = int(input())
for _ in range(t):
    n, m = [int(value) for value in input().split()]
    graph = Graph(n)
    for _ in range(m):
        x, y = [int(x) for x in input().split()]
        graph.connect(x - 1, y - 1)
    s = int(input())
    graph.find_all_distances(s - 1)
