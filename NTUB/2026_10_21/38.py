"""
positive: find 2 nagative
"""
d=list(map(int,input().split()))
naga=[0]*len(d)
posi=[0]*len(d)
if d[0]<0:
    naga[0]=d[0]
elif d[0]>0:
    posi[0]=d[0]
for rs in range(1,len(d)):
    if d[rs]>0:
        bot=1
        if posi[rs-1]!=0:
            bot=posi[rs-1]
        posi[rs]=d[rs]*bot
        if naga[rs-1]!=0:
            naga[rs]=d[rs]*naga[rs-1]

    elif d[rs]<0:
        if naga[rs-1]!=0:
            posi[rs]=d[rs]*naga[rs-1]

        bot=1
        if posi[rs-1]!=0:
            bot=posi[rs-1]
        naga[rs]=d[rs]*bot
print(max(posi))
"""
8 2 7 -8 3 5 -6 9 1 -2 -10
"""