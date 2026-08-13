
m,n,p=list(map(int,input().split()))
taken=[]
ever=set()
def recursion(lm=m,ln=n,lp=p,t1=0,t2=0,t3=0):
    global taken,ever
    if lm<0 or ln<0 or lp<0:
        return 0
    """
    bug occur
    """
    to_cheak=tuple([t1,t2,t3])
    if to_cheak in ever:
        return 0
    ever.add(to_cheak)

    if lm==0 and ln==0 and lp==0:
        taken.append([t1,t2,t3])
        return 0
    recursion(lm-2,ln-1,lp,t1+1,t2,t3)
    recursion(lm-1,ln-1,lp-1,t1,t2+1,t3)
    recursion(lm,ln-2,lp-3,t1,t2,t3+1)
def get():
    global taken,m,n,p
    recursion()
    for rs in taken:
        if rs[0]*2+rs[1]==m and rs[0]+rs[1]+rs[2]*2==n and rs[1]+rs[2]*3==p:
            return 1
    return 0
if get():
    print("YES")
else:
    print("NO")
"""

three child recursion tree

get every well taken


cheak if legal
"""