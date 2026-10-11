n=int(input())
res=0
for rs in range(1,n+1):
    if n%rs==0:
        res+=rs

print(res)