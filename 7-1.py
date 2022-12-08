#!/usr/bin/env python3

import json
from collections import Counter

cmd = ''
disk = {'/': {'size':0, 'files': [], 'subdirs': {}}}
current_dir = '/'

def get_dir(directory):
    path = directory.split('/')
    cdir = disk['/']
    for d in path[1:]:
        if len(d) > 0:
            cdir = cdir['subdirs'][d]
    return cdir

with open('in.7', 'r') as fd:
    for line in fd:
        # print(line[:-1])
        # print(json.dumps(disk, indent=2))
        if line.startswith('$'):
            # Command
            if line[2:].startswith('cd'):
                # Change dir
                cmd = 'cd'
                if line[5:-1] == '/':
                    currend_dir = '/'
                elif line[5:-1] in get_dir(current_dir)['subdirs'].keys():
                    if current_dir == '/':
                        current_dir += line[5:-1]
                    else:
                        current_dir += '/' + line[5:-1]
                elif line[5:-1] == '..':
                    path = current_dir.split('/')
                    current_dir = '/'.join(path[:-1])
            elif line[2:].startswith('ls'):
                # List
                cmd = 'ls'
        elif line.startswith('dir'):
            # subdir
            if line[5:-1] not in get_dir(current_dir)['subdirs'].keys():
                get_dir(current_dir)['subdirs'][line[4:-1]] = {'size':0, 'files': [], 'subdirs': {}}
            else:
                print(f'see {line[5:-1]} second time')
        elif line[0] in '0123456789':
            # file
            size, name = line.split()
            get_dir(current_dir)['files'].append({'size': int(size), 'name': name})
            get_dir(current_dir)['size'] += int(size)
            # Update subdir sizes
            temp_path = current_dir.split('/')
            temp_path.pop()
            while len(temp_path) > 0:
                get_dir('/'.join(temp_path))['size'] += int(size)
                temp_path.pop()
        # print(json.dumps(disk, indent=2))
        # print('current:', current_dir)
        # input()

# print(json.dumps(disk, indent=2))

# Walk the tree and sub up all directories having size of 
# less or equal to 100000
def sum_up_subdir_sizes(directory):
    # print(f"look into {directory}")
    summe = 0
    for d in get_dir(directory)['subdirs'].keys():
        if get_dir('/'.join([directory, d]))['size'] <= 100000:
            size = get_dir('/'.join([directory, d]))['size']
            # print(f"{'/'.join([directory, d])}: {size}")
            summe += size
        summe += sum_up_subdir_sizes('/'.join([directory, d]))
    return summe

summe = sum_up_subdir_sizes('/')

print(summe)
