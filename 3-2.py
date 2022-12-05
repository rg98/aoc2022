#!/usr/bin/env python3

from collections import Counter

def get_priority(ch):
    c = ord(ch)
    if c >= ord('a') and c <= ord('z'):
        return 1 + c - ord('a')
    elif c >= ord('A') and c <= ord('Z'):
        return 27 + c - ord('A')
    else:
        raise RuntimeError(f"Unexpected character: {chr(c)}")

priority_sum = 0

with open('in.3', 'r') as fd:
    group = []
    for line in fd:
        group.append(line[:-1])
        if len(group) == 3:
            one = Counter(group[0])
            two = Counter(group[1])
            three = Counter(group[2])
            badge = list(one & two & three)[0]
            priority_sum += get_priority(badge)
            group = []

print(priority_sum)

