#!/usr/bin/env python3

from collections import Counter

head = {'x':0, 'y':0}
tail = {'x':0, 'y':0}

tail_path = [(0, 0)]

# Moves:
# head moves always in direction
# tail adjusts

def move_left(n, head, tail):
    for i in range(n):
        head['x'] -= 1
        if tail['x'] - head['x'] > 1:
            if tail['y'] != head['y']:
                tail['y'] = head['y']
            tail['x'] -= 1
        tail_path.append((tail['x'], tail['y']))

def move_right(n, head, tail):
    for i in range(n):
        head['x'] += 1
        if head['x'] - tail['x'] > 1:
            if tail['y'] != head['y']:
                tail['y'] = head['y']
            tail['x'] += 1
        tail_path.append((tail['x'], tail['y']))

def move_up(n, head, tail):
    for i in range(n):
        head['y'] += 1
        if head['y'] - tail['y'] > 1:
            if tail['x'] != head['x']:
                tail['x'] = head['x']
            tail['y'] += 1
        tail_path.append((tail['x'], tail['y']))

def move_down(n, head, tail):
    for i in range(n):
        head['y'] -= 1
        if tail['y'] - head['y'] > 1:
            if tail['x'] != head['x']:
                tail['x'] = head['x']
            tail['y'] -= 1
        tail_path.append((tail['x'], tail['y']))

with open('in.9', 'r') as fd:
    for move in fd:
        direction, steps = move.split()
        if direction == 'L':
            move_left(int(steps), head, tail)
        elif direction == 'R':
            move_right(int(steps), head, tail)
        elif direction == 'U':
            move_up(int(steps), head, tail)
        elif direction == 'D':
            move_down(int(steps), head, tail)
        else:
            raise RuntimeError(f"Unexpected direction: {direction}")

print(len(list(Counter(tail_path))))

