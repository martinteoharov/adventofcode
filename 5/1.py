import sys
import numpy as np
from numpy import interp
import re

lines = [[int(i) for i in re.findall(r"\d+", l)] for l in sys.stdin.readlines()]

input, ranges = lines[:1][0], np.array(
    [l if len(l) == 3 else [-1, -1, -1] for l in lines[1:]]
)
for idx, _ in enumerate(input):
    print(f"seed: {input[idx]}")
    reset = True

    for drs, srs, lr in ranges:
        if drs == -1 and srs == -1 and lr == -1:
            reset = True
            continue

        src_range, dest_range = [srs, srs + lr], [drs, drs + lr]
        print(f"num: {input[idx]} src range: {src_range}, dest range: {dest_range}")
        if srs <= input[idx] < (srs + lr) and reset:
            input[idx] = interp(input[idx], src_range, dest_range)
            reset = False

print(input)
