"""
way = sum child way
0 coin = 1
but without order
"""
coins , target=list(map(int,input().split()))
d=list(map(int,input().split()))
dp=[0]*(target+1)
dp[0]=1

for coin in d:
    for ind in range(target+1):
        if ind-coin>=0:
            dp[ind]+=dp[ind-coin]
print((dp[target])%(10**9+7))
"""
3 6
2 3 5
"""