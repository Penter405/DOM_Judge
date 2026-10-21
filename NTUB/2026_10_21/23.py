who=dict()
bot=["I","V","X","L","C","D","M"]
money=dict()
value=[1,5,10,50,100,500,1000]
for rs in range(len(bot)):
    who[bot[rs]]=rs

for rs in range(len(bot)):
    money[bot[rs]]=value[rs]

res=0
last=None
for rs in input():
    if last!=None and who[last]<who[rs]:
        res-=money[last]*2
    res+=money[rs]
    last=rs

print(res)
    