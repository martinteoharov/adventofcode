import re
import sys

lines = [list(map(int, re.findall(r".\d+", line))) for line in sys.stdin.readlines()]


def calc_diffs(lines):
    curr = lines[-1]
    if all(v == 0 for v in curr):
        return lines

    lines.append([curr[i + 1] - curr[i] for i in range(0, len(curr) - 1)])
    return calc_diffs(lines)


s = 0
for line in lines:
    diffs = calc_diffs([line])
    last = diffs[-1]
    last.append(0)

    for diff in reversed(diffs[:-1]):
        diff.append(diff[-1] + last[-1])
        last = diff

    print(diffs[0])

    s += diffs[0][-1]

print(s)
