#!/usr/bin/env python3

import networkx as nx

grid = []
with open('in.12', 'r') as fd:
    for line in fd:
        row = list(map(lambda c: ord(c) - ord('a'), list(line[:-1])))
        grid.append(row)

for y, row in enumerate(grid):
    l = len(row)
    for x, col in enumerate(row):
        # Detect start and end and adjust levels
        if col == -14: # Found start
            start = y * l + x
            grid[y][x] = 0
        if col == -28: # Found end
            end = y * l + x
            grid[y][x] = 25

e = []

h = len(grid)
for y, row in enumerate(grid):
    l = len(row)
    for x, col in enumerate(row):
        # Create edges
        if x > 0: # Left
            if grid[y][x] + 1 >= grid[y][x-1]:
                e.append((y*l+x, y*l+x-1))
        if y > 0: # Top
            if grid[y][x] + 1 >= grid[y-1][x]:
                e.append((y*l+x, (y-1)*l+x))
        if x < l - 1: # Right
            if grid[y][x] + 1 >= grid[y][x+1]:
                e.append((y*l+x, y*l+x+1))
        if y < h - 1: # Bottom
            if grid[y][x] + 1 >= grid[y+1][x]:
                e.append((y*l+x, (y+1)*l+x))


G = nx.MultiDiGraph(e)

# Extract all coordinates having a value of 0 ('a')
min_path = len(row) * len(grid[0])
for y, row in enumerate(grid):
    l = len(row)
    for x, col in enumerate(row):
        if grid[y][x] == 0:
            try:
                path = nx.shortest_path(G, source=y*l+x, target=end)
            except nx.exception.NetworkXNoPath as err:
                continue
            if len(path) - 1 < min_path:
                min_path = len(path) - 1

print(min_path)
