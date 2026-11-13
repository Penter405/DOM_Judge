"""amount=int(input())
d=list(map(int,input().split()))

min_bought=d[0]
profit=0
now=0
for data in d:
    now+=data
    got=now-min_bought
    profit=max(profit,got)
    min_bought=min(min_bought,now)
print(profit)
"""
amount=int(input())
d=list(map(int,input().split()))
dp=[0]*len(d)
#hold or give up
for index in range(len(d)):
    if index==0:
        dp[0]=d[index]
    else:
        dp[index]=max(dp[index-1],0)+d[index]
print(max([0]+dp))