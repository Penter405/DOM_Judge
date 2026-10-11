d=[]
res=[]
t=int(input())
for _ in range(t):
    d.append(int(input()))
    d.sort()
    if len(d)%2==0:
        res.append(int((d[len(d)//2-1]+d[len(d)//2])/2))
    else:
        res.append(int(d[len(d)//2]))
for rs in res:
    print(rs)
"""
7
1
3
4
60
70
50
2
0 0 0 0
"""