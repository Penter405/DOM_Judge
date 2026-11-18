amount, sizeof=list(map(int,input().split()))
bags=[]
for _ in range(amount):
    bags.append(list(map(int,input().split())))
dp=[0]*(sizeof+1)
for weight,worth in bags:
    for index in range(len(dp)-1,weight-1,-1):
        if dp[index-weight]!=0 or index==weight:
            dp[index]=max(dp[index],dp[index-weight]+worth)

print(max(dp))