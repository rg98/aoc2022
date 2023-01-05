#!/usr/bin/env python3
# lowestBit is taken form https://wiki.python.org/moin/BitManipulations (called lowestSet)

with open('in.17', 'r') as fd:
    data = fd.read()

gas:list[str] = list(data[:-1])

rocks_bits:list[list[int]] = [[0x03C], [0x010, 0x038, 0x010], [0x038, 0x008, 0x008],
                              [0x020, 0x020, 0x020, 0x020], [0x030, 0x030]]

cave_bits:list[int] = [0x3ff, 0x101, 0x101, 0x101]

top_rock = 0

def rotate(l:list):
    first = l.pop(0)
    l.append(first)

def show_cave():
    for r in reversed(cave):
        print(r)

def decode_bits(b:int, r:int = 0) -> str:
    """Decode two bytes as chamber, which is seven
       units wide and infinitely high. The ground is marked
       as 0x3ff, which is one bit wider than the rest."""
    if b == 0x3ff:
        return '+-------+'
    else:
        s = '|'
        for i in range(7, 0, -1):
            bit = 1 << i
            if b & bit:
                s += '#'
            elif r & bit:
                s += '@'
            else:
                s += '.'
        s += '|'
        return s

def show_cave_bits(x:int = 0, y:int = 0, rock:list[int] = None):
    height = len(rock) if rock else 0
    for n, r in enumerate(reversed(cave_bits)):
        if rock == None:
            print(decode_bits(r))
        else:
            if len(cave_bits) - 1 - n >= y and len(cave_bits) - 1 - n <= y + height - 1:
                if x < 0:
                    rck = rock[len(cave_bits) - 1 - n - y] << -x
                else:
                    rck = rock[len(cave_bits) - 1 - n - y] >> x
                print(decode_bits(r, rck))
            else:
                print(decode_bits(r))

def get_top_rock(cave_bits:list[int]) -> int:
    for n in range(len(cave_bits) - 1, 0, -1):
        if 0xFE & cave_bits[n] != 0:
            return n
    return 0

def rock_fits(x:int, y: int, rock:list[int], cave_bits:list[int]):
    """Check if rock at position x, y does not collide with cave_bits
       x = 0 means initial position, two units from the left edge.
       y = 1 means lower bound of rock is on the ground."""
    
    def lowestBit(int_type):
        low = (int_type & -int_type)
        lowBit = -1
        while (low):
            low >>= 1
            lowBit += 1
        return(lowBit)

    low_bits = [lowestBit(n) for n in rock]
    low_bits.sort()
    if x < -2 or x > low_bits[0] - 1:
        return False
    if y < 1 or y > len(cave_bits) - len(rock):
        return False
    for i, r in enumerate(rock):
        if x < 0:
            if cave_bits[y+i] & (r << -x) != 0:
                return False
        else:
            if cave_bits[y+i] & (r >> x) != 0:
                return False
    return True

def drop_rock(rock:list[int], cave_bits:list[int], gas:list[str], show:bool = False):
    """Append rock to cave at hight top_rock + 3.
       Then drop the rock."""
    top = get_top_rock(cave_bits)
    print(f'append {len(cave_bits) - len(rock), top + 4}')
    for _ in range(len(cave_bits) - len(rock), top + 4):
        print('append one')
        cave_bits.append(0x101)
    current_row = top + 4 # len(cave_bits) - len(rock)
    x = 0
    while current_row > 0:
        # Move rock by gas if possible
        #if show:
        #    print(f'gas: {gas}')
        if gas[0] == '>':
            if show:
                print('try right')
            if rock_fits(x+1, current_row, rock, cave_bits):
                if show:
                    print('push right')
                x += 1
        elif gas[0] == '<':
            if show:
                print('try left')
            if rock_fits(x-1, current_row, rock, cave_bits):
                if show:
                    print('push left')
                x -= 1
        else:
            raise RuntimeError(f'Unexpected gas input: {gas[0]}!')
        rotate(gas)
        if show:
            show_cave_bits(x, current_row, rock)
        # Drop rock if possible
        if rock_fits(x, current_row - 1, rock, cave_bits):
            current_row -= 1
        else:
            for n, r in enumerate(rock):
                if x < 0:
                    cave_bits[current_row + n] |= (r << -x)
                else:
                    cave_bits[current_row + n] |= (r >> x)
            break
        if show:
            show_cave_bits(x, current_row, rock)

for n in range(2022):
    rock_height = len(rocks_bits[n % len(rocks_bits)])
    top_rock = get_top_rock(cave_bits)
    increment = 4 + top_rock + rock_height - len(cave_bits)
    print(f'append {increment} - height: {rock_height}, top: {top_rock}')
    for _ in range(increment):
        cave_bits.append(0x101)
    drop_rock(rocks_bits[n % len(rocks_bits)], cave_bits, gas)

print(get_top_rock(cave_bits))
