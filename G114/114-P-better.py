n=0
guy=[]
get=[]
for _ in range(int(input())):
    want=int(input())
    n=max(n,want)
    guy.append(want)
    get.append(0)

prime=[False,False]+[True]*(int(n**0.5+1)-1)
for rs in range(2,len(prime)):
    if prime[rs]:
        for bad in range(rs*2,len(prime),rs):
            prime[bad]=False
        all_1or0=True
        for i in range(len(get)):
            if guy[i]==rs and get[i]==0:
                get[i]=rs
                guy[i]=1
                continue
            while guy[i]!=0 and guy[i]%rs==0:
                guy[i]//=rs
                get[i]+=rs
            if get[i]!=0 and get[i] !=1:
                all_1or0=False
        if all_1or0:
            break

for rs in range(len(get)):
    if get[rs]==0:
        print(guy[rs])
    else:
        if guy[rs]!=0 and guy[rs]!=1:
            get[rs]+=guy[rs]
        print(get[rs])