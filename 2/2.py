# D2P2
import sys, re


def proc_game(input):
    game = {"red": 0, "green": 0, "blue": 0}
    for num, color in re.findall(r"(\d+) (\w+)|Game \d+", input):
        if color:
            game[color] = max(game[color], int(num))
    return game


print(
    sum(
        (lambda g: g["red"] * g["green"] * g["blue"])(proc_game(line))
        for line in sys.stdin.read().splitlines()
    )
)
