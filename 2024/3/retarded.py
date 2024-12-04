import re
import sys

state = '1'
expr = ''

def dont(): global state; state = '0'
def do(): global state; state = '1'
def mul(a, b): global expr; expr += f'+({int(a)*int(b)})*{state}'

input_text = sys.stdin.read().replace("don't()", "dont()")
exec(';'.join(re.findall(r"mul\(\d+,\d+\)|dont\(\)|do\(\)", input_text)))

print(eval(expr.lstrip('+')))