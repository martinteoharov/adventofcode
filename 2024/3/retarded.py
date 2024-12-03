import re
import sys

mul = lambda a, b: a * b  # noqa: E731
pattern = r"mul\(\d+,\d+\)|don't\(\)|do\(\)"

state = '1'
expression = ''
for instr in re.findall(pattern, sys.stdin.read()):
    if instr == "don't()":
        state = '0'
    elif instr == 'do()':
        state = '1'
    elif instr.startswith('mul'):
        expression += '+(' + instr + ')*' + state

print(eval(expression.lstrip('+')))