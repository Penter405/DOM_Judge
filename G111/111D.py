typ , total=list(map(int,input().split()))
coin=list(map(int,input().split()))
dp=[1]+[0]*total
for co in coin:
    for ind in range(len(dp)):
        if ind+co<=len(dp)-1:
            dp[ind+co]+=dp[ind]




print(dp[-1])
"""
3 9
2 3 5
"""