res=[]
for _ in range(int(input())):
    d=input()
    r=0
    for rs in range(16):
        
        if rs%2==0:
            bot=str(int(d[rs])*2)
        else:
            bot=str(int(d[rs]))
        if len(bot)==2:
            bot=int(bot[0])+int(bot[1])
        else:
            bot=int(bot[0])
        r+=bot
    if r%10==0:
        res.append("T")
    else:
        res.append("F")

print("\n".join(res))
"""
3
1234567891234561
4013735633800643
5181271099000014
5
1234567891234563
4013735633800642
5181271099000017
5241150318192904
5241150313182900
"""