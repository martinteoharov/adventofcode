import re
import sys

cards = [line for line in sys.stdin.readlines()]


def parse_input(card):
    pattern = ":(.*?)\|(.*)$"
    m = re.findall(pattern, card)[0]
    w, mine = [int(i) for i in filter(None, m[0].split(" "))], [
        int(i) for i in filter(None, m[1].split(" "))
    ]
    return w, mine


def rec_proc(idx, cards):
    card = cards[idx]
    w, m = parse_input(card)
    cl = len([n for n in m if n in w])

    # base statement
    if cl <= 0:
        return 1

    return 1 + sum([rec_proc(i, cards) for i in range(idx + 1, idx + cl + 1)])


print(sum([rec_proc(idx, cards) for idx, card in enumerate(cards)]))
