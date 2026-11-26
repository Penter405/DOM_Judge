d,time=list(map(int,input().split()))
for _ in range(time):
    if d%10==0:
        d//=10
    else:
        d-=1
print(d)