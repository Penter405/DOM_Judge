#find best solution?
#find min coin in need
coins,want=list(map(int,input().split()))
points=list(map(int,input().split()))
dp=[0]*(want+1)
for index in range(len(dp)):
    for point in points:
        if index-point>=0:
            if dp[index]!=0:
                dp[index]=min(dp[index],dp[index-point]+1)
            else:
                dp[index]=dp[index-point]+1
if dp[-1]==0:
    print(-1)
else:
    print(dp[-1])