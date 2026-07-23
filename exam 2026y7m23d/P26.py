dp=[1]
n=int(input())
for rs in range(1,n+1):
    dp.append(0)
    for pe in [1,2]:
        if rs-pe<0:
            continue
        else:
            dp[rs]+=dp[rs-pe]
print(dp[n])