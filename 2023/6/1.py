import math
import numpy as np
import sys
import re

lines = [[int(x) for x in re.findall(r"\d+", line)] for line in sys.stdin.readlines()]

races = list(zip(lines[0], lines[1]))

acc = []
for race in races:
    time, distance = race
    wins = 0
    print(f"Race: {race}")

    for s in range(0, time):
        travelled = s * (time - s)
        if travelled > distance:
            wins += 1

    print(wins)
    acc.append(wins)

print(np.prod(acc))
