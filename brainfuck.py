import sys
m=sys.stdin.read().split()
p=m.pop(0)
s=x=y=0
if m:s=list(m[0])
d=[0]*9**5
b={}
l=len(p)
for i in range(l):
	if p[i]=='[':d.append(i)
	if p[i]==']':u=d.pop();b[u],b[i]=i,u
while y<l:
	c=ord(p[y])
	x+=c==62;x-=c==60;d[x]+=c<44;d[x]-=c==45
	if c==46:print chr(d[x])
	if c==44:d[x]=ord(s.pop(0)) if s else -1
	if (d[x]==0)*c==91:y=b[y]
	if c>92:y=b[y]-1
	y+=1