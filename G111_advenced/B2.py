res=[]
for rs in range(int(input())):
    d=list(map(int,input().split()))
    d.sort()
    if d.count(d[0])==4:
        res.append("square")
    elif d[0]==d[1] and d[2]==d[3]:
        res.append("rectangle")
    elif sum(d)-d[-1]>=d[-1]:
        res.append("quadrangle")
    else:
        res.append("banana")

print("\n".join(res))
"""
4
10 8 7 6
9 1 9 1
29 29 29 29
5 12 30 7
"""