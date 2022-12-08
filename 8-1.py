#!/usr/bin/env python3

trees = []
with open('in.8', 'r') as fd:
    for row in fd:
        trees_row = []
        for tree in row[:-1]:
            trees_row.append(int(tree))
        trees.append(trees_row)

def top_view(height, x, y, trees):
    for _y in range(y):
        if trees[_y][x] >= height:
            return False
    return True

def bottom_view(height, x, y, trees):
    for _y in range(y+1, len(trees)):
        if trees[_y][x] >= height:
            return False
    return True

def left_view(height, x, y, trees):
    for _x in range(x):
        if trees[y][_x] >= height:
            return False
    return True

def right_view(height, x, y, trees):
    for _x in range(x+1, len(trees[0])):
        if trees[y][_x] >= height:
            return False
    return True

def is_visible(x, y, trees):
    if x == 0 or y == 0 or x == len(trees[0]) - 1 or y == len(trees) - 1:
        return True
    else:
        # Test four neighbors top, bottom, left and right
        # we need to test from the edge
        tree_height = trees[y][x]
        if top_view(tree_height, x, y, trees):
            return True
        elif bottom_view(tree_height, x, y, trees):
            return True
        elif left_view(tree_height, x, y, trees):
            return True
        elif right_view(tree_height, x, y, trees):
            return True

# Count visible trees
count = 0
for y in range(len(trees)):
    for x in range(len(trees[0])):
        if is_visible(x, y, trees):
            count += 1

print(count)
