#!/usr/bin/env python3

score = 0

def get_score(opp, me):
    # A: Rock,    B: Paper,    C: Scissors
    # X: Rock(1), Y: Paper(2), Z: Scissors(3)
    # Rock > Scissor, Scissor > Paper, Paper > Rock
    if opp == 'A' and me == 'X':
        # rock vs rock =
        return 1 + 3
    elif opp == 'A' and me == 'Y':
        # rock vs paper <
        return 2 + 6
    elif opp == 'A' and me == 'Z':
        # rock vs scissoors >
        return 3 + 0
    elif opp == 'B' and me == 'X':
        # paper vs rock >
        return 1 + 0
    elif opp == 'B' and me == 'Y':
        # paper vs paper =
        return 2 + 3
    elif opp == 'B' and me == 'Z':
        # paper vs scissoors <
        return 3 + 6
    elif opp == 'C' and me == 'X':
        # scissor vs rock <
        return 1 + 6
    elif opp == 'C' and me == 'Y':
        # scissor vs paper >
        return 2 + 0
    else:
        # scissor vs scissor =
        return 3 + 3

with open('in.2', 'r') as fd:
    for line in fd:
        opponent, me = line.split()
        score += get_score(opponent, me)

print(score)
