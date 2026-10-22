get=[]
n=0
amount=int(input())
for _ in range(amount):
    want=int(input())
    n=max(n,want)
    get.append(want)

good=[]
prime=[False,False]+[True]*(n-1)
for rs in range(2,len(prime)):
    if prime[rs]:
        good.append(rs)
        for bad in range(rs*2,len(prime),rs):
            prime[bad]=False

def out(n):
    if prime[n]:
        return n
    res=0
    for p in good:
        if n==1:
            return res
        while n%p==0:
            n//=p
            res+=p
    return res
for me in range(amount):
    print(str(out(get[me])))
