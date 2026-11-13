#n bag
while True:
    try:
        want=int(input())
    except:
        break
    dp=[0]*(want+1)
    dp[0]=1
    for index in range(len(dp)):
        for point in range(1,7):
            if index-point>=0:
                dp[index]+=dp[index-point]
        dp[index]=dp[index]%(10**9+7)
            

    print(dp[-1]%(10**9+7))