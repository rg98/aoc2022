#!/usr/bin/env python3

cubes = []

mmx = []
mmy = []
mmz = []

with open('in.18', 'r') as fd:
    for line in fd:
        x, y, z = list(map(lambda c: int(c), line[:-1].split(',')))
        if len(mmx) == 0:
            mmx = [x, x]
            mmy = [y, y]
            mmz = [z, z]
        else:
            if mmx[0] > x:
                mmx[0] = x
            elif mmx[1] < x:
                mmx[1] = x
            if mmy[0] > y:
                mmy[0] = y
            elif mmy[1] < y:
                mmy[1] = y
            if mmz[0] > z:
                mmz[0] = z
            elif mmz[1] < z:
                mmz[1] = z
        cubes.append([x, y, z])

cubes.sort()

# print(mmx)
# print(mmy)
# print(mmz)

grid = []
for z in range(mmz[0], mmz[1] + 1):
    grid.append([])
    for y in range(mmy[0], mmy[1] + 1):
        grid[z-mmz[0]].append([])
        for x in range(mmx[0], mmx[1] + 1):
            if [x, y, z] in cubes:
                grid[z-mmz[0]][y-mmy[0]].append(1)
            else:
                grid[z-mmz[0]][y-mmy[0]].append(0)
# print(len(grid))
# print(len(grid[0]))
# print(len(grid[0][0]))

n_cubes = 0
n_touches = 0
for z in range(mmz[0], mmz[1] + 1):
    for y in range(mmy[0], mmy[1] + 1):
        for x in range(mmx[0], mmx[1] + 1):
            if grid[z-mmz[0]][y-mmy[0]][x-mmx[0]] == 1:
                n_cubes += 1
                if x > mmx[0] and grid[z-mmz[0]][y-mmy[0]][x-mmx[0]-1] == 1:
                    # print('touch:', x, y, z,'-', x-1, y, z)
                    n_touches += 1
                if x < mmx[1] and grid[z-mmz[0]][y-mmy[0]][x-mmx[0]+1] == 1:
                    # print('touch:', x, y, z,'-', x+1, y, z)
                    n_touches += 1
                if y > mmy[0] and grid[z-mmz[0]][y-mmy[0]-1][x-mmx[0]] == 1:
                    # print('touch:', x, y, z,'-', x, y-1, z)
                    n_touches += 1
                if y < mmy[1] and grid[z-mmz[0]][y-mmy[0]+1][x-mmx[0]] == 1:
                    # print('touch:', x, y, z,'-', x, y+1, z)
                    n_touches += 1
                if z > mmz[0] and grid[z-mmz[0]-1][y-mmy[0]][x-mmx[0]] == 1:
                    # print('touch:', x, y, z,'-', x, y, z-1)
                    n_touches += 1
                if z < mmz[1] and grid[z-mmz[0]+1][y-mmy[0]][x-mmx[0]] == 1:
                    # print('touch:', x, y, z,'-', x, y, z+1)
                    n_touches += 1

print(f'cubes: {n_cubes} and {n_touches} touches')
print(n_cubes * 6 - n_touches)

