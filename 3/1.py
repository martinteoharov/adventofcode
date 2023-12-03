import sys
import re

# load all lines in a 2D list (lines are also split by char)
lines = [[*line.replace(".", "d").replace("\n", "")] for line in sys.stdin.readlines()]
# func to check if a string contains a symbol
sym = lambda e: not e.isalnum()


# check if anything adjacent is a symbol
def is_adj(lines, li, ci):
    if sym(lines[li][ci - 1]) or sym(lines[li][min(ci + 1, len(lines[li]) - 1)]):
        return True

    if li > 0:
        top = lines[li - 1]
        if sym(top[ci]) or sym(top[min(ci + 1, len(top) - 1)]) or sym(top[ci - 1]):
            return True

    if li < len(lines) - 1:
        bottom = lines[li + 1]
        if (
            sym(bottom[ci])
            or sym(bottom[min(ci + 1, len(bottom) - 1)])
            or sym(bottom[ci - 1])
        ):
            return True

    return False


s = 0
for li, l in enumerate(lines):
    for m in re.finditer(r"\d+", "".join(l)):
        for i in range(m.start(), m.end()):
            if is_adj(lines, li, i):
                s += int(m.group())
                break

print(s)
