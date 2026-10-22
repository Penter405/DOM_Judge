res=[]
for _ in range(int(input())):
    res.append(list(map(int,input().split())))

res.sort()
for rs in res:
    print(rs[0],rs[1])
