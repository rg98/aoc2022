#!/usr/bin/env python3

from collections import Counter

message = ''

with open('in.6', 'r') as fd:
    message = fd.read()

for n in range(13, len(message)):
    if len(list(Counter(message[n-13:n+1]))) == 14:
        print(n+1)
        break
