from collections import defaultdict
from numpy import prod
import sys
import re

# load all lines in a 2D list (lines are also split by char)
lines = [[*line.replace(".", "d").replace("\n", "")] for line in sys.stdin.readlines()]
# func to check if a string contains a symbol
sym = lambda e: not e.isalnum()

gear_dict = defaultdict(list)


# check if anything adjacent is a symbol
def is_adj(lines, li, ci):
    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    mn, mx = 0, len(lines[li]) - 1

    for d in dirs:
        # constrain values between min and max
        nli, nci = min(max(li + d[0], mn), mx), min(max(ci + d[1], 0), mx)
        if lines[nli][nci] == "*":
            return True, (nli, nci)

    return False


s = 0
for li, l in enumerate(lines):
    for m in re.finditer(r"\d+", "".join(l)):
        for i in range(m.start(), m.end()):
            if is_adj(lines, li, i):
                _, loc = is_adj(lines, li, i)
                nli, nci = loc
                gear_dict[f"{nli}.{nci}"].append(int(m.group()))
                break

print(s)


s = 0
for v in gear_dict.values():
    print(v)
    if len(v) == 2:
        s += prod([int(i) for i in v])
print(s)
