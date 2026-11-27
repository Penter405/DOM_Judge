for _ in range(int(input())):
    dp=list(map(int,input().split()))
    for ind in range(1,len(dp)):
        dp[ind]=max(dp[ind],dp[ind]+dp[ind-1])
    print(max(dp))