n=int(input())
dp=[1]+[0]*n
def get(n):
    if n<0:
        return 0
    return dp[n]
for rs in range(1,len(dp)):
    dp[rs]=get(rs-1)+get(rs-2)

print(dp[-1])
    