import sys
m = sys.stdin.readline().split(" ")
p = m[0]
s = list(m[1]) if len(m) > 1 else []
dp = 0
d = [0]*30000
pp = 0
bracket_stack = []
brackets = {}
for i in range(len(p)):
    if p[i] == '[': bracket_stack.append(i)
    if p[i] == ']': brackets[bracket_stack.pop()] = i
for k in brackets.keys(): brackets[brackets[k]] = k
while pp < len(p):
    c = p[pp]
    if c == '>': dp += 1
    elif c == '<': dp -= 1
    elif c == '+': d[dp] += 1
    elif c == '-': d[dp] -= 1
    elif c == '.': print chr(d[dp])
    elif c == ',': d[dp] = ord(s.pop(0)) if s else -1
    elif c == '[' and not d[dp]: pp = brackets[pp]
    elif c == ']': pp = brackets[pp] - 1
    pp += 1
