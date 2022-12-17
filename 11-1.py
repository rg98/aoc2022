#!/usr/bin/env python3

class Monkey:
    _items: list
    _catched: list
    _test: int
    _true: int
    _false: int
    _op: dict

    def __init__(self, items, operation, test, test_true, test_false):
        self._items = items
        self._op = {'+': self._add, '*': self._mul}
        self._operation = self._op[(operation.split())[-2]]
        self._operand = (operation.split())[-1]
        self._test = int(test)
        self._true = test_true
        self._false = test_false
        self._counter = 0

    def _add(self, summand0, summand1):
        return summand0 + int(summand1)

    def _mul(self, factor0, factor1):
        if factor1 == 'old':
            return factor0 * factor0
        else:
            return factor0 * int(factor1)

    def catch(self, item):
        self._items.append(item)

    def round_step(self):
        if len(self._items) > 0:
            self._counter += 1
            item = self._items.pop(0)
            level = int(self._operation(item, self._operand) / 3)
            if (level % self._test) == 0:
                return level, self._true
            else:
                return level, self._false
        else:
            return None
        
    def state(self):
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

for n in range(20):
    for monkey in monkeys:
        res = monkey.round_step()
        while res != None:
            item, to = res
            monkeys[to].catch(item)
            res = monkey.round_step()


for monkey in monkeys:
    print(monkey._counter)

inspections = list(sorted(map(lambda m: m._counter, monkeys)))
print(inspections)

print(f'result: {inspections[-1] * inspections[-2]}')

