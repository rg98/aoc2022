#!/usr/bin/env python3

score = 0

def get_score(opp, me):
    # A: Rock,    B: Paper,    C: Scissors
    # X: Lose(0), Y: Draw(3),  Z: Win(6)
    # Rock > Scissor, Scissor > Paper, Paper > Rock
    if opp == 'A' and me == 'X':
        # rock - loose -> scissors
        return 3 + 0
    elif opp == 'A' and me == 'Y':
        # rock - draw -> rock
        return 1 + 3
    elif opp == 'A' and me == 'Z':
        # rock - win -> paper
        return 2 + 6
    elif opp == 'B' and me == 'X':
        # paper - loose -> rock
        return 1 + 0
    elif opp == 'B' and me == 'Y':
        # paper - draw ->  paper
        return 2 + 3
    elif opp == 'B' and me == 'Z':
        # paper - win -> scissors
        return 3 + 6
    elif opp == 'C' and me == 'X':
        # scissor - loose -> paper
        return 2 + 0
    elif opp == 'C' and me == 'Y':
        # scissors - draw -> scissors
        return 3 + 3
    elif opp == 'C' and me == 'Z':
        # scissors - win -> rock
        return 1 + 6
    else:
        raise RuntimeError(f"Unexpected input: {opp}, {me}")

with open('in.2', 'r') as fd:
    for line in fd:
        opponent, me = line.split()
        score += get_score(opponent, me)

print(score)
