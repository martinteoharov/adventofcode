import re
import sys

lines = [line for line in sys.stdin.readlines()]


def parse_input(card):
    pattern = ":(.*?)\|(.*)$"
    m = re.findall(pattern, card)[0]
    w, mine = [int(i) for i in filter(None, m[0].split(" "))], [
        int(i) for i in filter(None, m[1].split(" "))
    ]
    return w, mine


s = 0
for line in lines:
    w, m = parse_input(line)
    for n in m:
        if n in w:
            pass

    correct = len([n for n in m if n in w])
    if correct > 0:
        s += pow(2, correct - 1)

print(s)
