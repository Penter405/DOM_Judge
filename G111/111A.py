from collections import Counter
d=input()
c=dict(Counter(d))
res=[]
for rs in sorted(c.keys(),reverse=True):
    res.append([len(c)-c[rs],ord(rs),c[rs]])

for rs in sorted(res,reverse=True):
    print(rs[1],rs[2])
