#!/usr/bin/env python3

elfs = []

with open('in.23', 'r') as fd:
    n = 0
    for line in fd:
        plan = list(line[:-1])
        elfs.extend(list(map(lambda e: [e[0], n], 
                    list(filter(lambda p: p[1] == '#', enumerate(list(plan)))))))
        n += 1

rules = ['north', 'south', 'west', 'east']

def rotate(l):
    first = l.pop(0)
    l.append(first)

def test_direction(elf, elfs, rule):
    if rule == 'north':
        if [elf[0]  , elf[1]-1] in elfs or \
           [elf[0]+1, elf[1]-1] in elfs or \
           [elf[0]-1, elf[1]-1] in elfs:
            return False
    elif rule == 'south':
        if [elf[0]  , elf[1]+1] in elfs or \
           [elf[0]+1, elf[1]+1] in elfs or \
           [elf[0]-1, elf[1]+1] in elfs:
            return False
    elif rule == 'west':
        if [elf[0]-1, elf[1]] in elfs or \
           [elf[0]-1, elf[1]+1] in elfs or \
           [elf[0]-1, elf[1]-1] in elfs:
            return False
    elif rule == 'east':
        if [elf[0]+1, elf[1]] in elfs or \
           [elf[0]+1, elf[1]+1] in elfs or \
           [elf[0]+1, elf[1]-1] in elfs:
            return False
    return True

def has_neighbors(elf, elfs):
    if [elf[0]  , elf[1]-1] in elfs or \
       [elf[0]+1, elf[1]-1] in elfs or \
       [elf[0]+1, elf[1]  ] in elfs or \
       [elf[0]+1, elf[1]+1] in elfs or \
       [elf[0]  , elf[1]+1] in elfs or \
       [elf[0]-1, elf[1]+1] in elfs or \
       [elf[0]-1, elf[1]  ] in elfs or \
       [elf[0]-1, elf[1]-1] in elfs:
        return True
    return False

def do_round(elfs):
    planed_moves = []
    no_move = True
    for i, elf in enumerate(elfs):
        if has_neighbors(elf, elfs):
            for rule in rules:
                if test_direction(elf, elfs, rule):
                    if rule == 'north':
                        planed_moves.append([i, [elf[0], elf[1]-1]])
                        no_move = False
                        break
                    elif rule == 'south':
                        planed_moves.append([i, [elf[0], elf[1]+1]])
                        no_move = False
                        break
                    elif rule == 'west':
                        planed_moves.append([i, [elf[0]-1, elf[1]]])
                        no_move = False
                        break
                    elif rule == 'east':
                        planed_moves.append([i, [elf[0]+1, elf[1]]])
                        no_move = False
                        break
    while len(planed_moves) > 0:
        move = planed_moves.pop(0)
        duplicates = list(filter(lambda m: m[1] == move[1], planed_moves))
        if len(duplicates) > 0:
            for d in duplicates:
                planed_moves.pop(planed_moves.index(d))
            continue
        elfs[move[0]] = move[1]
    rotate(rules)
    return no_move

moved = True
n_rounds = 0
while moved and n_rounds < 10:
    moved = not do_round(elfs)
    elfs = sorted(elfs, key=lambda elf: (elf[1], elf[0]))
    # print(f"Round {n_rounds}: {len(elfs)} - {elfs}")
    n_rounds += 1

#print(elfs)
print(f"{n_rounds} rounds")

x = list(map(lambda elf: elf[0], elfs))
y = list(map(lambda elf: elf[1], elfs))

x.sort()
y.sort()

dim_x = x[-1] - x[0] + 1
dim_y = y[-1] - y[0] + 1
n = len(elfs)

empty_tiles = (dim_x * dim_y) - n
print(f"empty tiles: {empty_tiles}")
