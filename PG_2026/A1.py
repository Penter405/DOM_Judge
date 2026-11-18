d=int(input())
res=0
while d!=0:
    if d%2!=0:
        res+=1
    d//=2
print(res)