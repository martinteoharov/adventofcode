import sys

# D1P2
l2d = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}
s = 0
for line in sys.stdin.read().splitlines():
    for idx in range(0, len(line) + 1):
        for k, v in l2d.items():
            r = line[:idx].replace(k, str(v))
            # If we have replaced something
            if line[:idx] != r:
                d = len(line[:idx]) - len(r)
                line = r + line[idx - d :]
            else:
                line = r + line[idx:]

    digits = [d for d in line if d.isnumeric()]
    s += int(digits[0] + digits[-1])

print(s)
