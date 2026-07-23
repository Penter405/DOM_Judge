result=[]
n=int(input())
for rs in range(1,n+1):
    if n%rs==0:
        result.append(rs)
if len(result)==2:
    print(f"{n} is prime.")
else:
    aver=sum(result)/len(result)
    print(f"{aver:.2f}")
    new=[]
    for rs in result:
        new.append(str(rs))
    print(' '.join(new))