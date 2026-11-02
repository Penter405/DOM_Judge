res=[]
for _ in range(int(input())):
    dp=list(map(int,input().split()))
    for rs in range(1,len(dp)):
        dp[rs]+=max(dp[rs-1],0)
    res.append(max(dp))

for rs in res:
    print(rs)