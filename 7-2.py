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

disk_size = 70000000

free_space = disk_size - get_dir('/')['size']

need_to_be_freed = 30000000 - free_space

def list_dir_sizes(directory):
    # print(f"look into {directory}")
    dirs = {directory: get_dir(directory)['size']}
    for d in get_dir(directory)['subdirs'].keys():
        dirs.update(list_dir_sizes('/'.join([directory, d])))
    return dirs

dirs = list_dir_sizes('/')

dir_sizes = sorted(dirs.values())

for s in dir_sizes:
    if s >= need_to_be_freed:
        print(s)
        break

