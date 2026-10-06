def getans():
    ori=input()
    want=input()

    if ori=="" or want=="":
        return max(len(ori), len(want))
    dp=[[0 for _ in range(len(ori)+1)] for _ in range(len(want)+1)]

    """
    basic
    w  1
    aY 2
    n3 
    t
    """

    for y in range(len(want)+1):
        dp[y][0]=y

    for x in range(len(ori)+1):
        dp[0][x]=x


    for y in range(1,len(want)+1):
        for x in range(1,len(ori)+1):
            if ori[x-1]==want[y-1]:
                dp[y][x]=dp[y-1][x-1]
            else:
                dp[y][x]=min( dp[y-1][x], dp[y][x-1] , dp[y-1][x-1] )+1


    return (dp[-1][-1])


print(getans())