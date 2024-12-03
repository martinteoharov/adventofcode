import re
import sys

mul = lambda a, b: a * b  # noqa: E731
pattern = r"mul\(\d+,\d+\)|don't\(\)|do\(\)"

c, add = 0, True
for instr in re.findall(pattern, sys.stdin.read()):
    if instr == "don't()":
        add = False
    elif instr == "do()":
        add = True
    else:
        c += eval(instr) if add else 0

print(c)