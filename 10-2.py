#!/usr/bin/env python3

ticks = 0

x = 1

display= ''

with open('in.10', 'r') as fd:
    for instruction in fd:
        code = instruction.split()
        if len(code) == 1:
            # noop
            if ticks >= x - 1 and ticks <= x + 1:
                display += '#'
            else:
                display += '.'
            ticks = (ticks + 1) % 40
        else:
            opcode, argument = code
            if ticks >= x - 1 and ticks <= x + 1:
                display += '#'
            else:
                display += '.'
            ticks = (ticks + 1) % 40
            if ticks >= x - 1 and ticks <= x + 1:
                display += '#'
            else:
                display += '.'
            ticks = (ticks + 1) % 40
            x += int(argument)

print('ticks:', ticks)
print('x:', x)
print(display[0:40])
print(display[40:80])
print(display[80:120])
print(display[120:160])
print(display[160:200])
print(display[200:240])

# x = 1
#           1    1    2    2    3    3    
# 0....5....0....5....0....5....0....5....
# #              XXX
#  #..XXX
#     ##    XXX
#       ..XX    
#         ##  XXX
#           ..XX
#    XXX      ##
#               ..XXX
#                 ##
