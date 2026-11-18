coins, want=list(map(int,input().split()))
coin=list(map(int,input().split()))
coin.sort()
dp=[0]+[float("inf")]*want
for index in range(1,want+1):
    for take in coin:
        if index-take<0:
            break
        dp[index]=min(dp[index],dp[index-take]+1)

if dp[-1]==float("inf"):
    print(-1)
else:
    print(dp[-1])