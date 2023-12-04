import sys
import re

# load all lines in a 2D list (lines are also split by char)
lines = [[*line.replace(".", "d").replace("\n", "")] for line in sys.stdin.readlines()]
# func to check if a string contains a symbol
sym = lambda e: not e.isalnum()


# check if anything adjacent is a symbol
def is_adj(lines, li, ci):
    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    mn, mx = 0, len(lines[li]) - 1

    for d in dirs:
        # constrain values between min and max
        nli, nci = min(max(li + d[0], mn), mx), min(max(ci + d[1], 0), mx)
        if sym(lines[nli][nci]):
            return True

    return False


def find_adj_numbers():
    # Have a set of (line_idx, range())
    # ...

    # Check for nearby digits and get the index of the digit
    # ...

    # Check if digit is part of a larger number
    # by going through all of the ranges
    # ...

    pass


s = 0
for li, l in enumerate(lines):
    for m in re.finditer(r"\d+", "".join(l)):
        for i in range(m.start(), m.end()):
            if is_adj(lines, li, i):
                s += int(m.group())
                break

print(s)
