sizeof=int(input())
d=list(map(int,input().split()))
target=sum(d)
dp=[0]*(target+1)
dp[0]=1
for coin in d:
    for ind in range(target,coin-1,-1):
        if dp[ind-coin]==1:
            dp[ind]=1
ever=False
print(dp.count(1)-1)
for ind in range(1,target+1):
    if dp[ind]:
        if ever:
            print(' ',end='')
        print(ind,end='')
        ever=True
print()