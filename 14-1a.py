#!/usr/bin/env python3

from time import sleep

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

limits = min_max_coordinates(walls)

landscape_height = limits[3] + 2
landscape_width = limits[1] - limits[0] + 3 # 2 * landscape_height + 1

landscape = bytearray('.' * landscape_height * landscape_width, encoding='ascii')

def build_landscape(landscape:bytearray, height:int, width:int, walls: list[tuple[int,int]]):
    for y in range(0, height + 1):
        # for x in range(500 - height, 500 + height + 1):
        for x in range(limits[0], limits[1]+1):
            if is_wall((x, y), walls):
                #landscape[y * width + x - (500 - height)] = ord('.')
                landscape[y * width + x - limits[0]] = ord('#')

# Get next free place
def next_free(x: int, width: int, height: int, landscape:bytearray) -> tuple[int,int]:
    global limits
    y = 0
    try:
        while True:
            if y <= limits[3] and landscape[(y + 1) * width + x - limits[0]] == ord('.'):
                y += 1
                continue
            if y <= limits[3] and landscape[(y + 1) * width + x - limits[0] - 1] == ord('.'):
                x -= 1
                y += 1
                continue
            if y <= limits[3] and landscape[(y + 1) * width + x - limits[0] + 1] == ord('.'):
                x += 1
                y += 1
                continue
            break
    except IndexError as err:
        print(x, y, err)
        raise IndexError(err)
    return (x, y)

# Print walls and sand on grid
build_landscape(landscape, landscape_height, landscape_width, walls)

sand = 0
unit: tuple[int,int] = (500,0)
while unit[0] >= limits[0] and unit[0] <= limits[1] and unit[1] <= limits[3]: # unit != (500, 0):
    # Drop sand until is stops or vanishes
    unit = next_free(500, landscape_width, landscape_height, landscape)
    if unit[0] >= limits[0] and unit[0] <= limits[1] and unit[1] <= limits[3]:
        landscape[unit[1] * landscape_width + unit[0] - limits[0]] = ord('o')
        sand += 1

#for y in range(0, landscape_height + 1):
#    print(str(landscape[y * landscape_width: (y+1) * landscape_width], encoding='ascii'))
print(sand)
