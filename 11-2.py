#!/usr/bin/env python3

import datetime
from typing import Callable, Dict, List, TypeVar

Self = TypeVar("Self", bound="Monkey")

class Monkey:
    _items: List[int]
    _catched: List[int]
    _test: int
    _true: int
    _false: int
    _op: Dict[str, Callable[[Self, int, int], int]]

    def __init__(self:Self, items:List[int], operation:str, test:str, test_true:int, test_false:int) -> Self:
        self._items = items
        self._op = {'+': self._add, '*': self._mul}
        self._operation = self._op[(operation.split())[-2]]
        self._operand = (operation.split())[-1]
        self._test = int(test)
        self._true = test_true
        self._false = test_false
        self._counter = 0

    def _add(self:Self, summand0: int, summand1: int):
        return summand0 + int(summand1)

    def _mul(self:Self, factor0: int, factor1: int):
        if factor1 == 'old':
            return factor0 * factor0
        else:
            return factor0 * int(factor1)

    def catch(self:Self, item: int):
        self._items.append(item)

    def round_step(self:Self, divisor):
        if len(self._items) > 0:
            self._counter += 1
            item = self._items.pop(0)
            level = self._operation(item, self._operand) % divisor
            if (level % self._test) == 0:
                return level, self._true
            else:
                return level, self._false
        else:
            return None
        
    def state(self:Self):
        print(self._items, self._op, 
              self._operation, self._operand, self._test, 
              self._true, self._false)

monkeys = []

with open('in.11', 'r') as fd:
    items = []
    operation = None
    for line in fd:
        if line.startswith('Monkey'):
            continue
        elif line.startswith('  Starting items:'):
            line = line.replace(',', '')
            items = list(map(int, (line.split())[2:]))
        elif line.startswith('  Operation: new = old '):
            operation = line[14:-1]
        elif line.startswith('  Test: divisible by'):
            test = int((line.split())[-1])
        elif line.startswith('    If true:'):
            _true = int(line.split()[-1])
        elif line.startswith('    If false'):
            _false = int(line.split()[-1])
            monkeys.append(Monkey(items, operation, test, _true, _false))

divisor = 1
for monkey in monkeys:
    divisor *= monkey._test

for n in range(10000):
    # if n in [1, 20, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000]:
    #     print(f'Round {n} {datetime.datetime.now()}')
    #     for monkey in monkeys:
    #         print(monkey._counter)
    #         print(monkey._items)
    for monkey in monkeys:
        res = monkey.round_step(divisor)
        while res != None:
            item, to = res
            monkeys[to].catch(item)
            res = monkey.round_step(divisor)


#for monkey in monkeys:
#    print(monkey._counter)

inspections = list(sorted(map(lambda m: m._counter, monkeys)))
# print(inspections)

print(f'result: {inspections[-1] * inspections[-2]}')

