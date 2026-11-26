d=int(input())
res=0
for n in range(1,int(d**0.5)+1):
    if d%n==0:
        res+=n
        res+=d//n
print(res)