"""
by each node, go his bepointed
choose the longest one
keep the answer global and after traval all output it
"""
from sys import stdin
d=stdin.read().split("\n")[:-1]
for rs in range(0,len(d),3):
    nodes=int(d[rs])
    must=[(a,b) for a,b in eval(d[rs+1])]
    cost=[0]+eval(d[rs+2])#all 1 indexed
    be=[[] for _ in range(nodes+1)]
    point=[[] for _ in range(nodes+1)]
    beamount=[0]*(nodes+1)
    for required, me in must:# ->
        point[required].append(me)
        be[me].append(required)
        beamount[me]+=1#still have sub dnf
    dnf=True
    while dnf:
        dnf=False#if any not 0 and we dont solved this time
        for index in range(1,nodes+1):
            if beamount[index]==0:
                cost[index]+=max([0]+[cost[index] for index in be[index]])
                for pointed in point[index]:
                    beamount[pointed]-=1
            else:
                dnf=True
    print(max(cost))
