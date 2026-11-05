res=[]
for _ in range(int(input())):
    a,b=list(map(int,input().split()))
    buffer=[]
    while a>0:
        buffer.append( hex(a%b)[2:].upper() )
        a-=a%b
        a//=b
    if len(buffer)==0:
        buffer=["0"]
    res.append("".join(buffer[::-1]))

for rs in res:
    print(rs)