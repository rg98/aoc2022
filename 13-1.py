#!/usr/bin/env python3

from json import loads
from itertools import zip_longest
from copy import deepcopy

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

packets:list[Packet] = []
result = 0
for i in range(0, len(lines), 3):
    pair = i//3 + 1
    left = Packet(lines[i])
    right = Packet(lines[i+1])
    if left < right:
        result += pair

print(result)
