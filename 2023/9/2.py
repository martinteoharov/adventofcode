import re
import sys

lines = [
    list(map(int, re.findall(r"-\d+|\d+", line))) for line in sys.stdin.readlines()
]


def calc_diffs(lines):
    curr = lines[-1]
    if all(v == 0 for v in curr):
        return lines

    lines.append([curr[i + 1] - curr[i] for i in range(0, len(curr) - 1)])
    return calc_diffs(lines)


s = 0
for line in lines:
    print(f"processing line: {line}")
    diffs = calc_diffs([line])
    last = diffs[-1]
    last.insert(0, 0)

    for diff in reversed(diffs[:-1]):
        diff.insert(0, diff[0] - last[0])
        last = diff

    print(diffs)

    s += diffs[0][0]

print(s)
