#!/usr/bin/env python3

from copy import deepcopy
from collections import Counter

limit = 4000000

sensors:list[tuple[int,int]] = []
beacons:list[tuple[int,int]] = []

def manhatten_distance(s:tuple[int,int], b:tuple[int,int]):
    return abs(s[0] - b[0]) + abs(s[1] - b[1])

def sectors_overlap_or_touch(sectors: list[tuple[int,int]]):
    if len(sectors) > 1:
        for s in zip(sectors[:-1], sectors[1:]):
            if s[0][1] + 1 >= s[1][0]:
                return sectors.index(s[0])
            else:
                return -1

def merge_sectors(sectors: list[tuple[int,int]]) -> list[tuple[int,int]]:
    ns = deepcopy(sectors)
    #print(f'merge in: {ns}')
    o = sectors_overlap_or_touch(ns)
    #print(f'overlap: {o}')
    while len(ns) > 1 and o != -1:
        # Overlap or touch between o and o+1
        left = ns[o]
        right = ns[o+1]
        #print(f'left: {left}, right: {right}')
        if left[0] <= right[0] and left[1] > right[1]:
            #print(f'drop second: {left} - {right}')
            del ns[o+1]
        elif left[1] + 1 >= right[0]:     # touch
            #print(f'overlap or touch: {left} - {right}')
            ns[0] = (left[0], right[1])
            del ns[o+1]
        o = sectors_overlap_or_touch(ns)
        #print(f'overlap: {o}')
    #print(f'merge out: {ns}')
    return ns

def possible_beacon_positions(sensors:list[tuple[int,int]],
                              beacons:list[tuple[int,int]], ref_line:int):
    sectors:list[tuple[int,int]] = []
    for n, s in enumerate(sensors):
        dist = manhatten_distance(s, beacons[n])
        ref_dist = abs(ref_line - s[1])
        if ref_dist <  dist:
            sector = (s[0] - (dist - ref_dist), s[0] + (dist - ref_dist))
            #print(f's_x: {s[0]}, s_y: {s[1]}, dist: {dist}, ref_dist: {ref_dist}, sector: {sector}')
            sectors.append(sector)
            if len(sectors) > 1:
                sectors.sort()
                sectors = merge_sectors(sectors)
    if len(sectors) == 1 and sectors[0][0] <= 0 and sectors[0][1] >= limit:
            return []
    # Return list of holes between sectors
    possible_beacons = []
    for s0, s1 in zip(sectors[:-1], sectors[1:]):
        if s0[1] < s1[0]:
            possible_beacons.append(list(range(s0[1], s1[0])))
    return possible_beacons

with open('in.15', 'r') as fd:
    for line in fd:
        args = line.split()
        s_x = int(list(args[2].split('='))[1][:-1])
        s_y = int(list(args[3].split('='))[1][:-1])
        sensors.append((s_x, s_y))
        b_x = int(list(args[8].split('='))[1][:-1])
        b_y = int(list(args[9].split('='))[1])
        beacons.append((b_x, b_y))

for ref_line in range(0, limit+1):
    if ref_line % 100000 == 0:
        print(ref_line)
    positions = possible_beacon_positions(sensors, beacons, ref_line)
    if len(positions) > 0:
        print(positions, ref_line)

if len(positions) == 0:
    print('none')
