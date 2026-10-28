res=[]
for _ in range(int(input())):
    d=list(map(int,input().split(",")))
    last=None#can be B,R/S,F  R root big, S root small
    for rs in range(len(d)):
        now=[0]#left node right
        if rs*2+1>len(d)-1:
            continue
        now.append(d[rs*2+1])
        now.append(d[rs])
        if not(rs*2+2>len(d)-1):
            now.append(d[rs*2+2])

        we=None
        if len(now)==3:
            if now[1]<now[2]:
                we="RB"
            else:
                we="S"
        else:
            if now[1]<now[2] and now[2]<now[3]:
                we="B"
            elif now[2]<now[1] and now[2]<now[3]:
                we="S"
            elif now[2]>now[1] and now[2]>now[3]:
                we="R"
            else:
                last="F"
                break
        #cheaking
        if last==None:
            last=we
        else:
            new=""
            for good in we:
                if good in last:
                    new+=good
            if new=="":
                last="F"
                break
            last=new
    if last=="R" or last=="S":
        last="H"
    res.append(last)


for rs in res:
    print(rs)