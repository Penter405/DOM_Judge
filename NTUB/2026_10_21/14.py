station,size=list(map(int,input().split()))
used=0
biggest=0
out=0
for rs in range(1,station+1):
    off,on=list(map(int,input().split()))
    used-=off
    used+=on
    biggest=max(biggest,used)
    if out==0 and used>size:
        out=rs

print(used,out,biggest)
