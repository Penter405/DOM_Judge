"""
cheak if someone prime,   int(x**0.5)+1 until
"""
large=0
repeat=int(input())
d=[]
result=[]
for _ in range(repeat):
    a,b=list(map(int,input().split(",")))
    if a>b:
        b,a=a,b
    if b-2==a:
        large=max(large,a,b)
    d.append((a,b))
prime=[False,False]+[True]*(large-1)
for n in range(int(large**0.5)+2):
    if prime[n]:
        for bad in range(n*2,large+1,n):
            prime[bad]=False

for a,b in d:
    if b-2!=a or not(prime[b]) or not(prime[a]):
        print("N")
    else:
        print("Y")