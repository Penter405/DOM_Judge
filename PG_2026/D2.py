rank=[]
teams, qus=list(map(int,input().split()))
for team in range(1,teams+1):
    got=list(map(int,input().split()))
    rank.append( (sum(got), got.count(100),max(got), teams+1-team ,team)  )

rank.sort(reverse=True)
ran=0
for total,got100,large,idsmall,id in rank:
    ran+=1
    print(ran,id,total,got100,large)