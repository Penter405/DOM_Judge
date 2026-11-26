for _ in range(int(input())):
    d=input().split()
    integers=[int(''.join(d[ind:ind+2]),16) for ind in range(0,len(d),2)]
    now=sum(integers)
    now=hex(now)[2:]
    if len(now)>=5:
        now=int(now[0],16)+int(now[1:],16)
    now=now  ^ 0xffff
    now=hex(now)[2:].zfill(4)
    print(now)
