import sys

myinput = sys.stdin.readline().split(" ")
program = myinput[0]
stdin = list(myinput[1]) if len(myinput) > 1 else []

data_pointer = 0
data = [0] * 30000
program_pointer = 0

bracket_stack = []
brackets = {}
for i in range(len(program)):
    if program[i] == '[': bracket_stack.append(i)
    if program[i] == ']': brackets[bracket_stack.pop()] = i
for k in brackets.keys():
    brackets[brackets[k]] = k

while program_pointer < len(program):
    c = program[program_pointer]
    if c == '>': data_pointer += 1
    elif c == '<': data_pointer -= 1
    elif c == '+': data[data_pointer] += 1
    elif c == '-': data[data_pointer] -= 1
    elif c == '.': print chr(data[data_pointer])
    elif c == ',': data[data_pointer] = ord(stdin.pop()) if stdin else -1
    elif c == '[' and not data[data_pointer]: program_pointer = brackets[program_pointer]
    elif c == ']': program_pointer = brackets[program_pointer] - 1
    program_pointer += 1

