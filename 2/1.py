# D2P1
import re

max_game = {"red": 12, "green": 13, "blue": 14}


def proc_game(input) -> dict:
    regex = "Game \d+|\d+ \w+"
    game = {"idx": 0, "red": 0, "green": 0, "blue": 0}
    for i in re.findall(regex, input):
        res = re.split(" ", i)
        if res[0] == "Game":
            game["idx"] = res[1]
        else:
            game[res[1]] = max(game[res[1]], int(res[0]))

    return game


s = 0
while True:
    try:
        line = input()
    except EOFError:
        break

    game = proc_game(line)
    if (
        game["red"] <= max_game["red"]
        and game["green"] <= max_game["green"]
        and game["blue"] <= max_game["blue"]
    ):
        s += int(game["idx"])

print(s)
