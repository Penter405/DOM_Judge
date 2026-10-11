res=[]
d=int(input())
prime=[0,0]+[1]*(d)
for n in range(len(prime)):
    if prime[n]==1:
        while d%n==0:
            d=d//n
            res.append(str(n))
        for rs in range(n,len(prime),n):
            prime[rs]=0
    if d==1:
        break
print(" ".join(res))