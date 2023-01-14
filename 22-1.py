#!/usr/bin/env python3

import sys, traceback

landscape: list[tuple[int, int, int]] = []

path: list[int] = []

def decode_path(s:str) -> list[int]:
    instr = [ord(c) - ord('0') for c in list(s)]
    n = 0
    path: list[int] = []
    for inst in instr:
        if inst < 10:
            n = n*10 + inst
        else:
            path.append(n)
            if inst == 34:
                path.append(-90)
            elif inst == 28:
                path.append(-270)
            else:
                raise RuntimeError(f"Unexpected instruction {chr(inst+ord('0'))}")
            n = 0
    if n > 0:
        path.append(n)
    return path

def decode_landscape(s:str) -> list[list[int]]:
    d = { ' ': -1, '.': 0, '#': 1}
    tiles = [d[t] for t in list(s)]
    return tiles

def execute_path(max_x:int, max_y:int, landscape:list[list[int]], path:list[int]) -> tuple[int,int,int]:
    pos:tuple[int,int,int] = [0,0,0]
    pos[1] = [x for x in range(len(landscape[0])) if landscape[0][x] == 0][0]
    print(f'start position: {pos}')
    for s in path:
        # print(f'step: {s} - {pos}', end=' ')
        if s > 0:
            if pos[2] == 0:
                # Right
                try:
                    while s > 0:
                        if landscape[pos[0]][(pos[1]+1) % max_x] == 1:
                            break
                        elif landscape[pos[0]][(pos[1]+1) % max_x] == 0:
                            pos[1] = (pos[1] + 1) % max_x
                        else:
                            old_pos = pos[1]
                            while landscape[pos[0]][(pos[1]+1) % max_x] == -1:
                                pos[1] = (pos[1] + 1) % max_x
                            if landscape[pos[0]][(pos[1]+1) % max_x] == 0:
                                continue
                            else:
                                pos[1] = old_pos
                        s -= 1
                except IndexError as err:
                    print(f"Error {err} (right): {pos}, {s}\n{sys.exc_info()}")
            elif pos[2] == 90:
                # Up
                try:
                    while s > 0:
                        if landscape[(pos[0]-1) % max_y][pos[1]] == 1:
                            break
                        elif landscape[(pos[0]-1) % max_y][pos[1]] == 0:
                            pos[0] = (pos[0] - 1) % max_y
                        else:
                            old_pos = pos[0]
                            while landscape[(pos[0]-1) % max_y][pos[1]] == -1:
                                pos[0] = (pos[0] - 1) % max_y
                            if landscape[(pos[0]-1) % max_y][pos[1]] == 0:
                                continue
                            else:
                                pos[0] = old_pos
                        s -= 1
                except IndexError as err:
                    print(f"Error {err} (up): {pos}, {s}\n{sys.exc_info()}")
            elif pos[2] == 180:
                # Left
                try:
                    while s > 0:
                        if landscape[pos[0]][(pos[1]-1) % max_x] == 1:
                            break
                        elif landscape[pos[0]][(pos[1]-1) % max_x] == 0:
                            pos[1] = (pos[1] - 1) % max_x
                        else:
                            old_pos = pos[1]
                            while landscape[pos[0]][(pos[1]-1) % max_x] == -1:
                                pos[1] = (pos[1] - 1) % max_x
                            if landscape[pos[0]][(pos[1]-1) % max_x] == 0:
                                continue
                            else:
                                pos[1] = old_pos
                        s -= 1
                except IndexError as err:
                    print(f"Error {err} (left): {pos}, {s}")
                    faulthandler.dump_traceback()
            else:
                # Down
                try:
                    while s > 0:
                        if landscape[(pos[0]+1) % max_y][pos[1]] == 1:
                            break
                        elif landscape[(pos[0]+1) % max_y][pos[1]] == 0:
                            pos[0] = (pos[0] + 1) % max_y
                        else:
                            old_pos = pos[0]
                            while landscape[(pos[0]+1) % max_y][pos[1]] == -1:
                                pos[0] = (pos[0] + 1) % max_y
                            if landscape[(pos[0]+1) % max_y][pos[1]] == 0:
                                continue
                            else:
                                pos[0] = old_pos
                        s -= 1
                except IndexError as err:
                    print(f"Error {err} (down): {pos}, {s}")
                    traceback.print_exc()
        else:
            if s == -90:
                pos[2] = (pos[2] - 90) % 360
            else:
                pos[2] = (pos[2] + 90) % 360
        # print(f'- {pos}')

    return pos

def rebuild_landscape(max_y: int, max_x: int, landscape: list[list[int]]) -> list[list[int]]:
    rblsc: list[list[int]] = []
    for row in landscape:
        if len(row) < max_x:
            row += [-1] * (max_x - len(row))
        rblsc.append(row)
    return rblsc

with open('in.22', 'r') as fd:
    read_landscape = True
    for line in fd:
        if len(line) > 1:
            if read_landscape:
                landscape.append(decode_landscape(line[:-1]))
            else:
                path = decode_path(line[:-1])
        else:
            read_landscape = False

max_y, max_x = (len(landscape), max([len(x) for x in landscape]))
print(max_y, max_x)
landscape = rebuild_landscape(max_y, max_x, landscape)

#ldict = {-1:'_', 0:'.', 1:'#'}
#for row in landscape:
#    for c in row:
#        print(f'{ldict[c]}', end='')
#    print()

pos = execute_path(max_x, max_y, landscape, path)


print(pos)

direction = {0:0, 90:3, 180:2, 270:1}
result = 1000 * (pos[0] + 1) + 4 * (pos[1] + 1) + direction[pos[2]]
print(result)

