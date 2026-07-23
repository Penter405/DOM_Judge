result=[]
a,b=list(map(int,input().split()))

for rs in range(a,b+1):
    size=len(str(rs))
    buffer=0
    for pe in str(rs):
        buffer+=int(pe)**size
    if buffer==int(rs):
        result.append(str(rs))
print("\n".join(result))