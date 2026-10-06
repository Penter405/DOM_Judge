a=input()
b=input()
c=input()
dp=[[[0 for _ in range(len(c)+1)] for _ in range(len(b)+1) ]for _ in range(len(a)+1)]
for a1 in range(1,len(a)+1):
    for b1 in range(1,len(b)+1):
        for c1 in range(1,len(c)+1):
            if a[a1-1]==b[b1-1]==c[c1-1]:
                dp[a1][b1][c1]=dp[a1-1][b1-1][c1-1]+1
            else:
                dp[a1][b1][c1]=max(dp[a1-1][b1][c1] , dp[a1][b1-1][c1], dp[a1][b1][c1-1])
print(dp[len(a)][len(b)][len(c)])
