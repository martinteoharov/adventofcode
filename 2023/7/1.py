import sys
from collections import Counter

cvm = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
}


def count_letter_frequencies(s):
    return sorted(Counter(s).values(), reverse=True)


hands = [line.replace("\n", "").split(" ") for line in sys.stdin.readlines()]


def sort_hands(input):
    hand = input[0]
    strength = 0
    count = count_letter_frequencies(hand)
    print(count)

    if count == [5]:
        strength = 6
    elif count == [4, 1]:
        strength = 5
    elif count == [3, 2]:
        strength = 4
    elif count == [3, 1, 1]:
        strength = 3
    elif count == [2, 2, 1]:
        strength = 2
    elif count == [2, 1, 1, 1]:
        strength = 1
    elif count == [1, 1, 1, 1, 1]:
        strength = 0

    return (
        strength,
        cvm[hand[0]],
        cvm[hand[1]],
        cvm[hand[2]],
        cvm[hand[3]],
        cvm[hand[4]],
    )


sorted_hands = sorted(hands, key=sort_hands, reverse=False)
print(sorted_hands)

s = 0
for idx, hand in enumerate(sorted_hands):
    # print(f"rank: {idx + 1}: {int(hand[1])}, sum: {s}")
    rank = idx + 1
    s += int(hand[1]) * rank

print(s)
