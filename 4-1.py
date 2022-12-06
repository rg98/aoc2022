#!/usr/bin/env python3

from collections import Counter

count = 0

with open('in.4', 'r') as fd:
    for line in fd:
        a, b = line[:-1].split(',')
        a_1, a_2 = a.split('-')
        b_1, b_2 = b.split('-')
        c_a = Counter(range(int(a_1), int(a_2) + 1))
        c_b = Counter(range(int(b_1), int(b_2) + 1))
        if len(list(c_a & c_b)) == len(list(c_a)) or \
           len(list(c_a & c_b)) == len(list(c_b)):
           count += 1

print(count)
