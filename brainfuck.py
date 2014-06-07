import sys
m=sys.stdin.readline().split(" ")
p=m[0]
s=list(m[1]) if len(m)>1 else []
x=y=0
d=[]
b={}
for i in range(len(p)):
	if p[i] == '[':d.append(i)
	if p[i] == ']':b[d.pop()]=i
for k in b.keys():b[b[k]]=k
d=[0]*30000
while y<len(p):
	c=p[y]
	if c=='>':x+=1
	if c=='<':x-=1
	if c=='+':d[x]+=1
	if c=='-':d[x]-=1
	if c=='.':print chr(d[x])
	if c==',':d[x]=ord(s.pop(0)) if s else -1
	if c=='[' and not d[x]:y=b[y]
	if c==']':y=b[y]-1
	y+=1
