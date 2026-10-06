table=[0,0]+[1]*(10**6-1)
prime=[]
for rs in range(10**6+1):
    if table[rs]==1:
        prime.append(rs)
        for pe in range(rs**2,10**6+1,rs):
            table[pe]=0
res=[]
while True:
    d=int(input())
    if d==0:
        break
    f=d
    many=0
    do=[]
    for pri in prime:
        if f==1:
            break
        if f%pri==0:
            many+=1
            do.append(pri)
            while f%pri==0:
                f//=pri
        
    #print(f"{d}:{many}", do)
    res.append(f"{d} : {many}")


print("\n".join(res))