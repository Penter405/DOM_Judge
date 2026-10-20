res=0
for _ in range(5):
    a=list(map(int,input().split()))
    a.sort()
    if a[0]+a[1]>a[2]:
        res+=1

print(res)