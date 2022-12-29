#!/usr/bin/env python3

from time import sleep

sand:list[tuple[int,int]] = []
walls:list[tuple[int,int]] = []

with open('in.14', 'r') as fd:
    for wall in fd:
        walls.append([(int(t[0]), int(t[1])) for t in [(c.split(',')) for c in [ t for t in wall.split(' -> ')]]])

# Get minimum and maximum x and y values
def min_max_coordinates(walls: list[tuple[int,int]]) -> tuple[int, int, int, int]:
    min_x = +1e9
    min_y = +1e9
    max_x = -1e9
    max_y = -1e9
    for wall in walls:
        for c in wall:
            if c[0] < min_x:
                min_x = c[0]
            if c[0] > max_x:
                max_x = c[0]
            if c[1] < min_y:
                min_y = c[1]
            if c[1] > max_y:
                max_y = c[1]
    return (min_x, max_x, min_y, max_y)

# Check wall
def is_wall(coord: tuple[int,int], walls:list[tuple[int,int]]) -> bool:
    for wall in walls:
        for lines in zip(wall[:-1], wall[1:]):
            # Check direction
            if lines[0][1] == lines[1][1]:
                # horizontal line
                if coord[1] == lines[0][1]:
                    if lines[0][0] > lines[1][0]:
                        if coord[0] >= lines[1][0] and coord[0] <= lines[0][0]:
                            return True
                        else:
                            continue
                    else:
                        if coord[0] >= lines[0][0] and coord[0] <= lines[1][0]:
                            return True
                        else:
                            continue
                else:
                    continue
            else:
                # vertical line
                if coord[0] == lines[0][0]:
                    if lines[0][1] > lines[1][1]:
                        if coord[1] >= lines[1][1] and coord[1] <= lines[0][1]:
                            return True
                        else:
                            continue
                    else:
                        if coord[1] >= lines[0][1] and coord[1] <= lines[1][1]:
                            return True
                        else:
                            continue
                else:
                    continue
    return False

# Check sand
def is_sand(coord:tuple[int,int], sand:list[tuple[int,int]]) -> bool:
    if coord in sand:
        return True
    return False

limits = min_max_coordinates(walls)

# Get next free place
def next_free(x: int, walls:list[tuple[int,int]], sand:list[tuple[int,int]]) -> tuple[int,int]:
    global limits
    unit = (x, 0)
    while True:
        if not is_wall((unit[0], unit[1]+1), walls) and \
           not is_sand((unit[0], unit[1]+1), sand) and unit[1]+1 <= limits[3] + 1:
            unit = (unit[0], unit[1]+1)
            continue
        if not is_wall((unit[0]-1, unit[1]+1), walls) and \
           not is_sand((unit[0]-1, unit[1]+1), sand) and unit[1]+1 <= limits[3] + 1:
            unit = (unit[0]-1, unit[1]+1)
            continue
        if not is_wall((unit[0]+1, unit[1]+1), walls) and \
           not is_sand((unit[0]+1, unit[1]+1), sand) and unit[1]+1 <= limits[3] + 1:
            unit = (unit[0]+1, unit[1]+1)
            continue
        break
    return unit

# Print walls and sand on grid
unit: tuple[int,int] = (500,0)
while unit[0] >= limits[0] and unit[0] <= limits[1] and unit[1] <= limits[3]:
    unit = (500, 0)
    #for y in range(0, limits[3]+1):
    #    for x in range(limits[0], limits[1]+1):
    #        if is_wall((x, y), walls):
    #            print('#', end='')
    #        elif is_sand((x, y), sand):
    #            print('o', end='')
    #        elif (x,y) == unit:
    #            print('@', end='')
    #        else:
    #            if y == 0 and x == 500:
    #                print('x', end='')
    #            else:
    #                print('.', end='')
    #    print()
    #print()
    # Drop sand until is stops or vanishes
    unit = next_free(500, walls, sand)
    if unit[0] >= limits[0] and unit[0] <= limits[1] and unit[1] <= limits[3]:
        sand.append(unit)

print(len(sand))
for y in range(0, limits[3]+1):
    for x in range(limits[0], limits[1]+1):
        if is_wall((x, y), walls):
            print('#', end='')
        elif is_sand((x, y), sand):
            print('o', end='')
        elif (x,y) == unit:
            print('@', end='')
        else:
            if y == 0 and x == 500:
                print('x', end='')
            else:
                print('.', end='')
    print()
