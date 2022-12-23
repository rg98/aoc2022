#!/usr/bin/env python3

import json

monkeys = {}

with open('in.21', 'r') as fd:
    for line in fd:
        instr = line[:-1].split()
        if len(instr) == 2:
            monkeys[instr[0][:-1]] = int(instr[1])
        else:
            monkeys[instr[0][:-1]] = {
                'op1': instr[1],
                'operand': instr[2],
                'op2': instr[3]
            }

def calculate(monkey, monkeys):
    if isinstance(monkeys[monkey], int):
        return monkeys[monkey]
    else:
        if monkeys[monkey]['operand'] == '+':
            return calculate(monkeys[monkey]['op1'], monkeys) + \
                calculate(monkeys[monkey]['op2'], monkeys)
        elif monkeys[monkey]['operand'] == '-':
            return calculate(monkeys[monkey]['op1'], monkeys) - \
                calculate(monkeys[monkey]['op2'], monkeys)
        elif monkeys[monkey]['operand'] == '*':
            return calculate(monkeys[monkey]['op1'], monkeys) * \
                calculate(monkeys[monkey]['op2'], monkeys)
        elif monkeys[monkey]['operand'] == '/':
            return calculate(monkeys[monkey]['op1'], monkeys) / \
                calculate(monkeys[monkey]['op2'], monkeys)
        else:
            raise RuntimeError(f'Unexpected operaotr: {monkeys[monkey]["operand"]}')

result = calculate('root', monkeys)

print(result)
