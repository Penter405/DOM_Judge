for _ in range(int(input())):
    sizeof=int(input())
    d=list(map(int,input().split()))
    if max(d)<=0:
        print("Losing streak.")
        continue
    dp=[d[0]]+[0]*(sizeof-1)
    for ind in range(1,sizeof):
        dp[ind]=max(dp[ind-1],0)+d[ind]
    print("The maximum winning streak is {}.".format(max(dp)))