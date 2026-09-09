"""

 (1,           ROOT)        (2       ,L)(3,      R)(4,RL )       
"""
place=dict()
radd=dict()
data=input().replace(" ","").replace("(","").strip().split(")")[:-1]
for bot in data:
    name, address=bot.split(',')
    address=address.replace("ROOT","A")
    radd[address]=name
    place[name]=address


same=[]
p,q=input().split(',')
times=-1
if len(place[p])>len(place[q]):
    times=len(place[q])
else:
    times=len(place[p])

for index in range(times):
    if place[p][index]==place[q][index]:
        same.append(place[p][index])
    else:
        break
if len(same)==0:
    print(radd['A'])
else:
    target=''.join(same)
    print(radd[target])