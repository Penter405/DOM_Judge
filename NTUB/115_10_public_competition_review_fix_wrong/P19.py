sizeof=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

evera=[False]*sizeof
everb=[False]*sizeof
ra=rb=0
for rs in range(sizeof):
    ra+=a[rs]
    if a[rs]==10:
        if rs+1<sizeof:
            evera[rs+1]=True
        if rs+2<sizeof:
            evera[rs+2]=True
    if evera[rs]:
        ra+=a[rs]


    rb+=b[rs]
    if b[rs]==10:
        if rs+1<sizeof:
            everb[rs+1]=True
        if rs+2<sizeof:
            everb[rs+2]=True
    if everb[rs]:
        rb+=b[rs]

if ra==rb:
    print(0)
elif ra>rb:
    print(1)
else:
    print(2)    
