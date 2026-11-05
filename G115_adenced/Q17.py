data=[]
for _ in range(int(input())):
    data.append(int(input()))
res=[]
for rs in data:
    res.append(rs)
    res.sort()
    bot=(len(res)-1)//2
    if len(res)%2==0:
        print((res[bot]+res[bot+1])//2)
    else:
        print(res[bot])
