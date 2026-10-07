u=input()
d=list(map(int,input().split()))
d.sort()
taking=0
res=0
for rs in d:
    taking+=rs
    res+=taking

print(res)