#!/usr/bin/env python3

from json import dumps, loads
from itertools import zip_longest

with open('in.13', 'r') as fd:
    data = fd.read()

lines = data.splitlines()

class Packet:
    _obj: dict

    def __init__(self, s):
        self._obj = loads(s)

    def __str__(self):
        return dumps(self._obj)

    def __lt__(self, other):
        return self.compare(self._obj, other._obj) == 1

    def __eq__(self, other):
        return self._obj == other._obj

    def compare(self, a, b):
        if isinstance(a, int) and isinstance(b, int):
            if a < b:
                return 1
            elif a > b:
                return -1
            else:
                return 0
        elif isinstance(a, int):
            a = [a]
        elif isinstance(b, int):
            b = [b]
        # Now both values are lists
        for p, q in zip_longest(a, b):
            if p == None:
                return 1
            elif q == None:
                return -1
            r = self.compare(p, q)
            if r != 0:
                return r
        return 0

packets: list[Packet] = []
for i in range(0, len(lines), 3):
    packets.append(Packet(lines[i]))
    packets.append(Packet(lines[i+1]))

p1 = Packet('[[2]]')
p2 = Packet('[[6]]')
packets.append(p1)
packets.append(p2)

P = sorted(packets)

print((P.index(p1)+1) * (P.index(p2)+1))

