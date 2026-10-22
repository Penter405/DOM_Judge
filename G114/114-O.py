n=0
def formating(s):
    for rs in range(len(s)):
        if s[rs]!="0":
            return s[rs:]
def rever(n):
    return int(formating(str(n)[::-1]))
get=[]
for _ in range(int(input())):
    want=int(input())
    n=max(n,want,rever(want))
    get.append(want)


prime=[False,False]+[True]*(n-1)
for rs in range(2,n+1):
    if prime[rs]:
        for bad in range(rs*2,n+1,rs):
            prime[bad]=False
res=[]
for want in get:
    if prime[want]:
        if rever(want)!=want and prime[rever(want)]:
            res.append(f"{want} is an emirp number.")
        else:
            res.append(f"{want} is a prime number.")
    else:
        res.append(f"{want} is not a prime number.")

print("\n".join(res))
"""
6
17
18
19
179
199
131

"""