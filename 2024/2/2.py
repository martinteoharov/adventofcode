import sys

reports = [list(map(int, line.strip().split())) for line in sys.stdin]

# p1
rc = sum(
    all(
        (report[0] < report[1]) == (prev < curr) and 1 <= abs(prev - curr) <= 3
        for prev, curr in zip(report, report[1:])
    )
    for report in reports
)

print(rc)


# p2
rc = 0

for report in reports:
    
    for fallidx in range(-1, len(report)):
        cpy = report[:fallidx] + report[fallidx + 1:] if fallidx >= 0 else report
        asc = cpy[0] < cpy[1]

        invalid = any(
            (asc and cpy[i] > cpy[i + 1]) or
            (not asc and cpy[i] < cpy[i + 1]) or
            not (1 <= abs(cpy[i] - cpy[i + 1]) <= 3)
            for i in range(len(cpy) - 1)
        )

        if not invalid:
            break

    if invalid:
        continue

    rc += 1

print(rc)