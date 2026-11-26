res=[]
d=int(input())
for n in range(2,int(d**0.5)+2):
    while d%n==0:
        d//=n
        res.append(str(n))
    if d==1:
        break
if d!=1:
    res.append(str(d))
print(' '.join(res))