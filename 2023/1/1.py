import sys
import re

print(
    sum(
        [
            int("".join([re.findall(r"\d", l)[0], re.findall(r"\d", l)[-1]]))
            for l in sys.stdin.readlines()
        ]
    )
)
