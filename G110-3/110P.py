u=input()
d=list(map(int,input().split()))
dp=[1]+[0]*sum(d)
for rs in d:
    for ind in range(len(dp)-1,-1,-1):
        if ind-rs<0:
            break
        if dp[ind-rs]==1:
            dp[ind]=1
res=[]
for rs in range(1,len(dp)):
    if dp[rs]==1:
        res.append(str(rs))

print(dp.count(1)-1)
print(" ".join(res))