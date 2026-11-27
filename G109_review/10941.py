"""
find achievable
combination-> for coin first
"""

from sys import stdin
d=stdin.read().split('\n')
for line in d:
    if line=='':
        continue
    line=list(map(int,line.split()))
    dp=[0]*(line[0]+1)
    dp[0]=1
    for coin in line[2:]:
        for ind in range(len(dp)-1,coin-1,-1):
            if dp[ind-coin]:
                dp[ind]=ind
    print(max(dp))