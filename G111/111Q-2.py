u=input()
d=list(map(int,input().split()))
res=0
while len(d)!=1:
    a=d.pop(d.index(min(d)))
    b=d.pop(d.index(min(d)))
    res+=(a+b)
    d.append(a+b)

print(res)