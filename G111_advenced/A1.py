a=list(map(int,input().split()))
b=list(map(int,input().split()))
res=0
for r,s in zip(a,b):
    res+=r*s

print(res)