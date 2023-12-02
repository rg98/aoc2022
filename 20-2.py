#!/usr/bin/env python3

from copy import deepcopy

code = []
npos = -1

with open('in.20', 'r') as fd:
    l = 0
    for num in fd:
        code.append((l, int(num[:-1]) * 811589153))
        if code[-1][1] == 0 and npos == -1:
            npos = l
        l += 1

print(f'{len(code)} codes')

key = [n for n in code]

def rearrange(i, arr):
    pos = arr.index(i)
    arr.pop(pos)
    npos = (pos + i[1]) % len(arr)
    arr.insert(npos, i)

for i in range(10):
    for k in key:
        rearrange(k, code)
        # print(code)

null_pos = code.index((npos, 0))
coord_x = code[(null_pos + 1000) % len(code)][1]
coord_y = code[(null_pos + 2000) % len(code)][1]
coord_z = code[(null_pos + 3000) % len(code)][1]

print(coord_x)
print(coord_y)
print(coord_z)

print(coord_x+coord_y+coord_z)
