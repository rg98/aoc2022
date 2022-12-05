#!/usr/bin/env python3

elfs = {}
n_elfs = 0

with open('in.1', 'r') as fd:
    for line in fd:
        line = line[:-1]
        if len(line) > 0:
            if n_elfs in elfs.keys():
                elfs[n_elfs]['list'].append(int(line))
            else:
                elfs[n_elfs] = {'list': [], 'value': 0}
                elfs[n_elfs]['list'].append(int(line))
        else:
            elfs[n_elfs]['value'] = sum(elfs[n_elfs]['list'])
            n_elfs += 1

elfs[n_elfs]['value'] = sum(elfs[n_elfs]['list'])

sorted_elfs = list(sorted(elfs.items(), key=lambda item: -item[1]['value']))

print(sorted_elfs[0][1]['value'] + sorted_elfs[1][1]['value'] + sorted_elfs[2][1]['value'])

