import sys
m=sys.stdin.readline().split()
p=m.pop(0)
s=x=y=0
if m:s=list(m[0])
d=[0]*30000
b={}
l=len(p)
for i in range(l):
	if p[i]=='[':d.append(i)
	if p[i]==']':u=d.pop();b[u],b[i]=i,u
while y<l:
	c=p[y]
	if c=='>':x+=1
	if c=='<':x-=1
	if c in '+-':d[x]+=int(c+'1')
	if c=='.':print chr(d[x])
	if c==',':d[x]=ord(s.pop(0)) if s else -1
	if (d[x]==0)*c=='[':y=b[y]
	if c==']':y=b[y]-1
	y+=1