res=0
for _ in range(5):
    d=list(map(int,input().split()))
    d.sort()
    if d[2]<d[1]+d[0]:
        res+=1
print(res)