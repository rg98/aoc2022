#!/usr/bin/env python3

count = 0

with open('in.4', 'r') as fd:
    for line in fd:
        a, b = line[:-1].split(',')
        a_1, a_2 = a.split('-')
        b_1, b_2 = b.split('-')
        a_1 = int(a_1)
        a_2 = int(a_2)
        b_1 = int(b_1)
        b_2 = int(b_2)
        print(a_1, a_2, b_1, b_2)
        if a_1 <= b_1 and a_2 >= b_2:
            print('b in a')
            count += 1
        elif a_1 >= b_1 and a_2 <= b_2:
            print('a in b')
            count += 1

print(count)
