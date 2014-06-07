import sys
m = sys.stdin.readline().split(" ")
p = m[0]
s = list(m[1]) if len(m) > 1 else []

data_pointer = 0
d = [0]*30000
program_pointer = 0

bracket_stack = []
brackets = {}
for i in range(len(p)):
    if p[i] == '[': bracket_stack.append(i)
    if p[i] == ']': brackets[bracket_stack.pop()] = i
for k in brackets.keys():
    brackets[brackets[k]] = k

while program_pointer < len(p):
    c = p[program_pointer]
    if c == '>': data_pointer += 1
    elif c == '<': data_pointer -= 1
    elif c == '+': d[data_pointer] += 1
    elif c == '-': d[data_pointer] -= 1
    elif c == '.': print chr(d[data_pointer])
    elif c == ',': d[data_pointer] = ord(s.pop(0)) if s else -1
    elif c == '[' and not d[data_pointer]: program_pointer = brackets[program_pointer]
    elif c == ']': program_pointer = brackets[program_pointer] - 1
    program_pointer += 1

