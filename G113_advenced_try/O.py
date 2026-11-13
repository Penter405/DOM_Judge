#find best solution?
#find min coin in need
coins,want=list(map(int,input().split()))
points=list(map(int,input().split()))
dp=[float("inf")]*(want+1)
dp[0]=0
for index in range(len(dp)):
    for point in points:
        if index-point>=0:
            dp[index]=min(dp[index],dp[index-point]+1)
if dp[-1]==float("inf"):
    print(-1)
else:
    print(dp[-1])