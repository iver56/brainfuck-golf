import sys
m = sys.stdin.readline().split(" ")
p = m[0]
s = list(m[1]) if len(m) > 1 else []
dp = 0
pp = 0
d=[]
brackets = {}
for i in range(len(p)):
    if p[i] == '[': d.append(i)
    if p[i] == ']': brackets[d.pop()] = i
for k in brackets.keys(): brackets[brackets[k]] = k
d=[0]*30000
while pp < len(p):
    c = p[pp]
    if c == '>': dp+=1
    if c == '<': dp-=1
    if c == '+': d[dp]+=1
    if c == '-': d[dp]-=1
    if c == '.': print chr(d[dp])
    if c == ',': d[dp]=ord(s.pop(0)) if s else -1
    if c == '[' and not d[dp]: pp=brackets[pp]
    if c == ']': pp=brackets[pp]-1
    pp+=1
