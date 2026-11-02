res=[]
for _ in range(int(input())):
    d=eval(input())
    d1=[]
    d2=[]
    for a,b in d:
        d1.append(a)
        d2.append(b)
    ans=0
    dp=[[0 for _ in range(max(d1)+1)] for _ in range(max(d2)+1)]
    for a,b in d:
        dp[b][a]=1
    for b in range(1,len(dp)):
        for a in range(1,len(dp[0])):
            dp[b][a]=max(dp[b][a]+dp[b-1][a-1],dp[b-1][a],dp[b][a-1])
            ans=max(ans,dp[b][a])
    res.append(ans)

for rs in res:
    print(rs)