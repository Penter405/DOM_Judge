from sys import stdin
data=list(map(int,stdin.read().split()))
large=max(data)


dp=[1]+[0]*large
for coin in 1,5,10,25,50:
    for index in range(large+1):
    
        if index+coin<len(dp) and dp[index]!=0:
            dp[index+coin]+=dp[index]

for line in data:
    print(dp[line])
"""
0
17
11
4
1000
2000
7489
"""