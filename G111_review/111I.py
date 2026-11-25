n=int(input())
gla=[['0','1']]
for _ in range(1,n):
    res=[]
    for guy in gla[-1]:
        res.append('0'+guy)
    for guy in gla[-1][::-1]:
        res.append('1'+guy)
    gla.append(res)
for line in gla[-1]:
    print(line)