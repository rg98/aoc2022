#!/usr/bin/env python3

from collections import Counter

def get_priority(first, second):
    c_first = Counter(first)
    c_second = Counter(second)
    common = c_first & c_second
    c = ord(list(common)[0])
    if c >= ord('a') and c <= ord('z'):
        return 1 + c - ord('a')
    elif c >= ord('A') and c <= ord('Z'):
        return 27 + c - ord('A')
    else:
        raise RuntimeError(f"Unexpected character: {chr(c)}")

priority_sum = 0

with open('in.3', 'r') as fd:
    for line in fd:
        compartment_size = int(len(line) / 2)
        first = line[0:compartment_size]
        second = line[compartment_size:-1]
        priority_sum += get_priority(first, second)

print(priority_sum)

