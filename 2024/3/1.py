import re
import sys

mul = lambda a, b: a * b  # noqa: E731
pattern = r"mul\(\d+,\d+\)"

line = sys.stdin.readlines()[0]
instructions = re.findall(pattern, line)

c = 0
for i in instructions:
    c += eval(i)
