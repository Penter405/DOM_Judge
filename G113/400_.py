from collections import Counter
u=input()
d=list(map(int,input().split()))
d=dict(Counter(d))
good=None
friend=[]
for guy, time in d.items():
    if good==None or time>good:
        friend=[guy]
        good=time
        
    elif time==good:
        friend.append(guy)
friend.sort()
for rs in friend:
    print(rs,good)
"""
12
2 4 2 3 2 5 3 7 2 3 4 3
12
1 1 1 3 3 4 4 3 4 2 2 2

"""