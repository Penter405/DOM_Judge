import math
for _ in range(int(input())):
    a,b=list(map(int,input().split()))
    aa=math.sqrt(a)
    bb=math.sqrt(b)
    if aa!=int(aa):
        aa=int(aa)+1
    aa=int(aa)
    bb=int(bb)
    if bb==aa:
        print(1)
    elif aa<bb:
        print(bb-aa+1)
    else:
        print(0)