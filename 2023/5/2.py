import sys
import numpy as np
from numpy import interp
import re

# Read and parse lines
lines = [[int(i) for i in re.findall(r"\d+", l)] for l in sys.stdin.readlines()]

# Process input and ranges
input_values, raw_ranges = np.array(lines[0]), lines[1:]

# Generate input array using vectorized operations
input_array = np.concatenate(
    [
        np.arange(start, start + count)
        for start, count in zip(input_values[::2], input_values[1::2])
    ]
)

# Filter and precompute source and destination ranges
precomputed_ranges = [
    (srs, srs + lr, drs, drs + lr)
    for drs, srs, lr in raw_ranges
    if len(drs, srs, lr) == 3
]

# Apply interpolation
for idx, (srs, srs_end, drs, drs_end) in enumerate(precomputed_ranges):
    mask = (input_array >= srs) & (input_array < srs_end)
    input_array[mask] = interp(input_array[mask], [srs, srs_end], [drs, drs_end])

    # Print progress
    print(f"Processing range {idx + 1}/{len(precomputed_ranges)}", end="\r")

# Calculate the minimum value
min_value = np.min(input_array)
print("\nMinimum value:", min_value)
