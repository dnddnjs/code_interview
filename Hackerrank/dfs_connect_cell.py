""" DFS: Connected Cell in a Grid
author : Woongwon Lee
problem : https://www.hackerrank.com/challenges/ctci-connected-cell-in-a-grid/problem
output : Print the number of cells in the largest region in the given matrix.
"""


class Graph:
    def __init__(self, grid):
        self.grid = grid

    def get_regions(self, row, column):
        if (0 <= row < len(self.grid) and
            0 <= column < len(self.grid[0]) and
                    self.grid[row][column] == 1):
            self.grid[row][column] = 0
            child_list = [[row - 1, column - 1],
                          [row    , column - 1],
                          [row + 1, column - 1],
                          [row - 1, column    ],
                          [row + 1, column    ],
                          [row - 1, column + 1],
                          [row    , column + 1],
                          [row + 1, column + 1]]
            return 1 + sum(self.get_regions(child[0], child[1])
                           for child in child_list)
        return 0


def getBiggestRegion(grid):
    g = Graph(grid)
    regions = []

    for row in range(len(grid)):
        for column in range(len(grid[0])):
            if grid[row][column] == 1:
                region = g.get_regions(row, column)
                regions.append(region)
    return max(regions)


n = int(input().strip())
m = int(input().strip())
grid = []
for grid_i in range(n):
    grid_t = list(map(int, input().strip().split(' ')))
    grid.append(grid_t)
print(getBiggestRegion(grid))