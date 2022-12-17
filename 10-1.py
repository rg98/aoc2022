#!/usr/bin/env python3

ticks = 0

x = 1

check = 20
check_interval = 40

result = 0

with open('in.10', 'r') as fd:
    for instruction in fd:
        code = instruction.split()
        # print(code)
        if len(code) == 1:
            opcode = code[0]
            if ticks + 1 >= check:
                result += x * check
                check += check_interval
                # print(f'- ticks: {ticks+1}, x: {x}, check: {check}, result: {result}')
            ticks += 1
            # print(f'ticks: {ticks}, x: {x}, check: {check}')
        else:
            opcode, argument = code
            if ticks + 2 >= check:
                result += x * check
                check += check_interval
                # print(f'- ticks: {ticks+2}, x: {x}, check: {check}, result: {result}')
            ticks += 2
            x += int(argument)
            # print(f'ticks: {ticks}, x: {x}, check: {check}')

print('ticks:', ticks)
print('x:', x)
print(result)
