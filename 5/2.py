import sys
import numpy as np
from numpy import interp
import re

lines = [[int(i) for i in re.findall(r"\d+", l)] for l in sys.stdin.readlines()]

input_values, ranges = np.array(lines[0]), np.array(
    [l if len(l) == 3 else [-1, -1, -1] for l in lines[1:]]
)

inp = np.concatenate(
    [
        np.arange(start, start + count)
        for start, count in zip(input_values[::2], input_values[1::2])
    ]
)

print("before copy")
# Copy inp to a mutable array
input_array = np.copy(inp)
print("after copy")

for idx in range(len(input_array)):
    reset = True

    for drs, srs, lr in ranges:
        if drs == -1:
            reset = True
            continue

        src_range, dest_range = [srs, srs + lr], [drs, drs + lr]

        if srs <= input_array[idx] < (srs + lr) and reset:
            input_array[idx] = interp(input_array[idx], src_range, dest_range)
            reset = False

min_value = np.min(input_array)
print(min_value)
