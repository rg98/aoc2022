#!/usr/bin/env python3

from collections import Counter

sensors = []
beacons = []

grid = []

def manhatten_distance(s, b):
    return abs(s[0] - b[0]) + abs(s[1] - b[1])

def impossible_beacon_positions(sensors, beacons, ref_line):
    beacons_in_ref_line = list(Counter(list(map(lambda b: b[0], \
                               filter(lambda b: b[1] == ref_line, beacons)))))
    scan_line = []
    for n, s in enumerate(sensors):
        dist = manhatten_distance(s, beacons[n])
        ref_dist = abs(ref_line - s[1])
        if ref_dist <  dist:
            # Add coordinates to list where beacon could not be
            scan_line.extend(list(range(s[0] - (dist - ref_dist),
                                        s[0] + dist - ref_dist + 1)))

    pos_list = list(Counter(scan_line))
    for pos in beacons_in_ref_line:
        pos_list.remove(pos)
    return pos_list

with open('in.15', 'r') as fd:
    for line in fd:
        args = line.split()
        s_x = int(list(args[2].split('='))[1][:-1])
        s_y = int(list(args[3].split('='))[1][:-1])
        sensors.append([s_x, s_y])
        b_x = int(list(args[8].split('='))[1][:-1])
        b_y = int(list(args[9].split('='))[1])
        beacons.append([b_x, b_y])

ref_line = 2000000

positions = len(impossible_beacon_positions(sensors, beacons, ref_line))

print(positions)
