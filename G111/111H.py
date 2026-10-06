u=input()
d=list(map(int,input().split()))
dp=[1]*len(d)
for ind in range(len(d)):
    best=0
    for did in range(ind):
        if d[did]<d[ind]:
            if dp[did]>best:
                best=dp[did]
    dp[ind]=max(dp[ind], best+1)

print(max(dp))