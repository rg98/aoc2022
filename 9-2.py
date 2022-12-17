#!/usr/bin/env python3

from collections import Counter

head = {'x':0, 'y':0}
tail = [{'x':0, 'y':0}, {'x':0, 'y':0}, {'x':0, 'y':0}, {'x':0, 'y':0},
        {'x':0, 'y':0}, {'x':0, 'y':0}, {'x':0, 'y':0}, {'x':0, 'y':0},
        {'x':0, 'y':0}]

tail_path = [(0, 0)]

# Moves:
# head moves always in direction
# tail adjusts

def tail_step(head, tail):
    # Determine distance between head and adjust tail
    if abs(head['x'] - tail['x']) > 1:
        # Then x position has moved and y position need to be adjusted as well
        if head['x'] - tail['x'] > 0:
            tail['x'] = head['x'] - 1
            tail['y'] = head['y']
        else:
            tail['x'] = head['x'] + 1
            tail['y'] = head['y']
    elif abs(head['y'] - tail['y']) > 1:
        # Then y position has moved and x position need to be adjusted as well
        if head['y'] - tail['y'] > 0:
            tail['y'] = head['y'] - 1
            tail['x'] = head['x']
        else:
            tail['y'] = head['y'] + 1
            tail['x'] = head['x']
    
def move_left(n, head, tail):
    for i in range(n):
        head['x'] -= 1
        a = head
        for n in range(len(tail)):
            b = tail[n]
            tail_step(a, b)
            a = b
        tail_path.append((tail[-1]['x'], tail[-1]['y']))

def move_right(n, head, tail):
    for i in range(n):
        head['x'] += 1
        a = head
        for n in range(len(tail)):
            b = tail[n]
            tail_step(a, b)
            a = b
        tail_path.append((tail[-1]['x'], tail[-1]['y']))

def move_up(n, head, tail):
    # print('up')
    for i in range(n):
        head['y'] += 1
        a = head
        for n in range(len(tail)):
            b = tail[n]
            tail_step(a, b)
            a = b
            # print(head, tail)
        tail_path.append((tail[-1]['x'], tail[-1]['y']))
    # print()

def move_down(n, head, tail):
    for i in range(n):
        head['y'] -= 1
        a = head
        for n in range(len(tail)):
            b = tail[n]
            tail_step(a, b)
            a = b
        tail_path.append((tail[-1]['x'], tail[-1]['y']))

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

#print(list(Counter(tail_path)))
print(len(list(Counter(tail_path))))

