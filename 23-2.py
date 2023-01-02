#!/usr/bin/env python3

elfs: set[tuple[int,int]] = set()

with open('in.23', 'r') as fd:
    n: int = 0
    for line in fd:
        plan:[str] = list(line[:-1])
        elfs |= (set(map(lambda e: (e[0], n), 
                      list(filter(lambda p: p[1] == '#', enumerate(plan))))))
        n += 1

rules:list[str] = ['north', 'south', 'west', 'east']

def rotate(l:list[str]):
    first = l.pop(0)
    l.append(first)

def test_direction(elf:tuple[int,int], elfs:set[tuple[int,int]], rule:str) -> bool:
    if rule == 'north':
        if set([(elf[0]  , elf[1]-1),
                (elf[0]+1, elf[1]-1),
                (elf[0]-1, elf[1]-1)]) & elfs:
            return False
    elif rule == 'south':
        if set([(elf[0]  , elf[1]+1),
                (elf[0]+1, elf[1]+1),
                (elf[0]-1, elf[1]+1)]) & elfs:
            return False
    elif rule == 'west':
        if set([(elf[0]-1, elf[1]),
                (elf[0]-1, elf[1]+1),
                (elf[0]-1, elf[1]-1)]) & elfs:
            return False
    elif rule == 'east':
        if set([(elf[0]+1, elf[1]),
                (elf[0]+1, elf[1]+1),
                (elf[0]+1, elf[1]-1)]) & elfs:
            return False
    return True

def has_neighbors(elf:tuple[int,int], elfs:set[tuple[int,int]]) -> bool:
    neighbors =  set([(elf[0]  , elf[1]-1),
                      (elf[0]+1, elf[1]-1),
                      (elf[0]+1, elf[1]  ),
                      (elf[0]+1, elf[1]+1),
                      (elf[0]  , elf[1]+1),
                      (elf[0]-1, elf[1]+1),
                      (elf[0]-1, elf[1]  ),
                      (elf[0]-1, elf[1]-1)])
    if neighbors & elfs:
        return True
    return False

def do_round(elfs:set[tuple[int,int]]) -> bool:
    planed_moves:list[tuple[tuple[int,int], tuple[int,int]]] = []
    no_move:bool = True
    for i, elf in enumerate(elfs):
        if has_neighbors(elf, elfs):
            for rule in rules:
                if test_direction(elf, elfs, rule):
                    if rule == 'north':
                        planed_moves.append((elf, (elf[0], elf[1]-1)))
                        no_move = False
                        break
                    elif rule == 'south':
                        planed_moves.append((elf, (elf[0], elf[1]+1)))
                        no_move = False
                        break
                    elif rule == 'west':
                        planed_moves.append((elf, (elf[0]-1, elf[1])))
                        no_move = False
                        break
                    elif rule == 'east':
                        planed_moves.append((elf, (elf[0]+1, elf[1])))
                        no_move = False
                        break
    while len(planed_moves) > 0:
        move = planed_moves.pop(0)
        duplicates = list(filter(lambda m: m[1] == move[1], planed_moves))
        if len(duplicates) > 0:
            for d in duplicates:
                planed_moves.pop(planed_moves.index(d))
            continue
        elfs.remove(move[0])
        elfs.add(move[1])
    rotate(rules)
    return no_move

moved:bool = True
n_rounds:int = 0
while moved:
    moved = not do_round(elfs)
    n_rounds += 1
    #print(f"Round {n_rounds} done")

# print(elfs)
print(f"{n_rounds} rounds")

#x = list(map(lambda elf: elf[0], elfs))
#y = list(map(lambda elf: elf[1], elfs))
#
#x.sort()
#y.sort()
#
#dim_x = x[-1] - x[0] + 1
#dim_y = y[-1] - y[0] + 1
#n = len(elfs)
#
#empty_tiles = (dim_x * dim_y) - n
#print(f"empty tiles: {empty_tiles}")
