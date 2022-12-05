#!/usr/bin/env python3

stacks = []

with open('in.5', 'r') as fd:
    stack_done = False
    stack_input = []
    instructions = []
    for line in fd:
        if not stack_done:
            if len(line) == 1:
                stack_done = True
                continue
            if '[' in line:
                stack_input.append(line)
            else:
                stacks = line.split()
        else:
            instructions.append(line[:-1])

for sin in stack_input:
    for n in range(len(stacks)):
        if '[' in sin[4*n:4*n+3]:
            if isinstance(stacks[n], str):
                stacks[n] = []
            stacks[n].append(sin[4*n+1:4*n+2])

for stack in stacks:
    stack = stack.reverse()

for instruction in instructions:
    moves, src, dest = instruction.split()[1:6:2]
    # print(f'move {int(moves)} from {int(src)} to {int(dest)}')
    for m in range(int(moves)):
        tmp = stacks[int(src)-1].pop()
        stacks[int(dest)-1].append(tmp)

result = ''
for stack in stacks:
    result += stack.pop()

print(result)
