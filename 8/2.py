import sys
import re
import itertools


lines = [l.replace("\n", "") for l in sys.stdin.readlines()]
instructions = lines[0]
START = [
    re.findall(r"[0-9A-Z]+", line)[0]
    for line in lines[2:]
    if re.findall(r"[0-9A-Z]+", line)[0].endswith("A")
]


def create_map(lines):
    map = {}
    for line in lines:
        matches = re.findall(r"[0-9A-Z]+", line)
        if matches[0] not in map:
            map[matches[0]] = (matches[1], matches[2])
    return map


map = create_map(lines[2:])
print(map)

keys = START
step = 0

for instruction in itertools.cycle(instructions):
    curr = []
    for key in keys:
        curr.append(map[key])

    all_found = True
    for key in keys:
        if not key.endswith("Z"):
            all_found = False

    if all_found:
        break

    if instruction == "L":
        for idx, key in enumerate(keys):
            keys[idx] = map[key][0]
    elif instruction == "R":
        for idx, key in enumerate(keys):
            keys[idx] = map[key][1]

    step += 1

print(step)
