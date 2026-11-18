"""
my_best=me+ previous best or previous best

"""
global_index=0
while True:
    global_index+=1
    a_size,b_size=list(map(int,input().split()))
    if a_size==0 and b_size==0:
        break
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    dp=[[0 for _ in range(b_size+1)] for _ in range(a_size+1)]  #b a
    large=0
    for y in range(1,a_size+1):
        for x in range(1,b_size+1):
            now=0
            if a[y-1]==b[x-1]:
                now=1

            dp[y][x]=max(now+dp[y-1][x-1],dp[y][x-1],dp[y-1][x])
            large=max(large,dp[y][x])
    print("Twin Towers #{}".format(global_index))
    print("Number of Tiles : {}".format(large))
"""
7 6
20 15 10 15 25 20 15
15 25 10 20 15 20
8 9
10 20 20 10 20 10 20 10
20 10 20 10 10 20 10 10 20
0 0


"""