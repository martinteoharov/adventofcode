import sys
import re
import itertools

START = "AAA"

lines = [l.replace("\n", "") for l in sys.stdin.readlines()]
instructions = lines[0]


def create_map(lines):
    map = {}
    for line in lines:
        matches = re.findall(r"[A-Z]+", line)
        if matches[0] not in map:
            map[matches[0]] = (matches[1], matches[2])
    return map


map = create_map(lines[2:])
print(map)

key = START
step = 0

for instruction in itertools.cycle(instructions):
    curr = map[key]
    print(f"{key} -> {curr} ({instruction})")
    if key == "ZZZ":
        break

    if instruction == "L":
        key = curr[0]
    elif instruction == "R":
        key = curr[1]

    step += 1

print(step)
