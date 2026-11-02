res=list()
for _ in range(int(input())):
    a,b=list(map(int,input().split()))
    res.append(a==b)

for rs in res:
    print(rs)