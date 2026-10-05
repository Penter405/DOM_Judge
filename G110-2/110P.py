"""
possible= sigma(times from that coin )


"""
useless=input()
coin=list(map(int,input().split()))
total=sum(coin)
dp=[1]+[0]*total

for rs in coin:
    for pe in range(total,-1,-1):
        if dp[pe]!=0:
            dp[pe+rs]=1


result=[]
for rs in range(1,total+1):
    if dp[rs]==1:
        result.append(str(rs))

print(len(result))
print(" ".join(result))