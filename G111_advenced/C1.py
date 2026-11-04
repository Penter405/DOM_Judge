big=0
d=[]
while True:
    x=int(input())
    if x==0:
        break
    big=max(big,x)
    d.append(x)
res=[0]*len(d)
im=[]
prime=[False,False]+[True]*(big-1)
for n in range(len(prime)):
    if prime[n]:
        im.append(n)
        for bad in range(n*2,len(prime),n):
            prime[bad]=False


for p in im:
    for index in range(len(res)):
        if prime[d[index]-p] and p<=d[index]-p:
            res[index]+=1

for rs in res:
    print(rs)
"""
8
20
42
10
12
4
0
"""