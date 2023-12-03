# D1P1
sum = 0
while True:
    try:
        line = input()
    except EOFError:
        break
    digits = [dig for dig in line if dig.isnumeric()]
    sum += int(digits[0] + digits[-1])
print(sum)
