#!/usr/bin/env python3

trees = []
with open('in.8', 'r') as fd:
    for row in fd:
        trees_row = []
        for tree in row[:-1]:
            trees_row.append(int(tree))
        trees.append(trees_row)

def top_view(height, x, y, trees):
    count = 0
    for _y in range(y-1, -1, -1):
        if trees[_y][x] < height:
            count += 1
        elif trees[_y][x] >= height:
            count += 1
            break
    return count

def bottom_view(height, x, y, trees):
    count = 0
    for _y in range(y+1, len(trees)):
        if trees[_y][x] < height:
            count += 1
        elif trees[_y][x] >= height:
            count += 1
            break
    return count

def left_view(height, x, y, trees):
    count = 0
    for _x in range(x-1, -1, -1):
        if trees[y][_x] < height:
            count += 1
        elif trees[y][_x] >= height:
            count += 1
            break
    return count

def right_view(height, x, y, trees):
    count = 0
    for _x in range(x+1, len(trees[0])):
        if trees[y][_x] < height:
            count += 1
        elif trees[y][_x] >= height:
            count += 1
            break
    return count

def scenic_score(x, y, trees):
    if x == 0 or y == 0 or x == len(trees[0]) - 1 or y == len(trees) - 1:
        return 0
    else:
        # Test four neighbors top, bottom, left and right
        # we need to test from the edge
        tree_height = trees[y][x]
        top = top_view(tree_height, x, y, trees)
        bottom =  bottom_view(tree_height, x, y, trees)
        left =  left_view(tree_height, x, y, trees)
        right = right_view(tree_height, x, y, trees)
        # print(f'x: {x}, y: {y}, t: {top}, b: {bottom}, l: {left}, r: {right}')
        return top * bottom * left * right

# Count visible trees
max_score = 0
for y in range(len(trees)):
    for x in range(len(trees[0])):
        score = scenic_score(x, y, trees)
        if score > max_score:
            max_score = score

print(max_score)
