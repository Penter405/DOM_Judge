good=[False,False]+[True]*65534
for n in range(65536):
    if good[n]:
        for bad in range(n+n,65536,n):
            good[bad]=False



res=[]
for _ in range(int(input())):
    bot=list(map(int,input().split(",")))
    bot.sort()
    if bot[0]+2!=bot[1]:
        res.append("N")
    elif good[bot[0]]==True and good[bot[1]]==True:
        res.append("Y")
    else:
        res.append("N")

for rs in res:
    print(rs)
            


