
res=[]
while True:
    try:
        bw=int(input())
    except:
        break
    king=None
    ans=0
    unique=set()
    n=int(input())
    for _ in range(n):
        me,value=list(map(int,input().split()))
        if king==None:
            king=me
        if me==king and value not in unique:
            unique.add(value)
            ans+=value
    res.append(ans)

for rs in res:
    print(rs)
"""
4
7
2 3
1 4
1 2
1 2
2 2
2 2
2 1
4
7
2 3
1 4
1 2
1 2
2 2
2 2
2 1
"""