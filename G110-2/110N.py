basic=input()
want=input()
dp=[  [0 for _ in range(len(basic)+1)] for _ in range(len(want)+1) ]
#print(dp)

for x in range(len(basic)+1):
    dp[0][x]=x
for y in range(len(want)+1):
    dp[y][0]=y
for b in range(1,len(want)+1):
    for a in range(1,len(basic)+1):
        if basic[a-1]==want[b-1]:
            dp[b][a]=dp[b-1][a-1]#dp[b-1][a] means you have count want first a element in it, so the cost is imcorrect
        else:
            dp[b][a]=min(dp[b-1][a-1],dp[b][a-1],dp[b-1][a])+1

print(dp[-1][-1])
#print(dp)