large=0
small=float("inf")
lasta=None
lastb=None
for _ in range(int(input())):
    a,b=list(map(int,input().split()))
    if lasta!=None:
        d=abs(lasta-a)+abs(lastb-b)
        large=max(large,d)
        small=min(small,d)
    lasta=a
    lastb=b


print(large,small)