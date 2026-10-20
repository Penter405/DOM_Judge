spe=set("[ ! @ # $ ^ & * ( ) , . ? ” : { } | < > ]".split())



good=[False]*4

pa=input()

for rs in pa:
    if "0"<=rs<="9":
        good[0]=True
    elif "A"<=rs<="Z":
        good[1]=True
    elif "a"<=rs<="z":
        good[2]=True
    elif rs in spe:
        good[3]=True

ans=0
if len(pa)>=8:
    ans+=1

ans+=good.count(True)
print(ans)