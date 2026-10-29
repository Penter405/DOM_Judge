res=[]
def cheak():
    a,b=sorted(list(map(int,input().split(","))))
    if b-2!=a:
        return False
    sizeof=int(b**0.5)+1
    prime=[False,False]+[True]*sizeof
    good=[a,b]
    for n in range(2,len(prime)):
        if prime[n]:
            for bad in range(n*2,len(prime)):
                prime[bad]=False

            for rs in range(2):
                if good[rs]%n==0 and good[rs] !=n:
                    return False
    return True
for _ in range(int(input())):
    if cheak():
        res.append("Y")
    else:
        res.append("N")

for rs in res:
    print(rs)