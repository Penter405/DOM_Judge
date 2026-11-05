pa=input()
good=[False]*4
me=set("[ ! @ # $ ^ & * ( ) , . ? ” : { } | < > ]".replace(" ",""))

for rs in pa:
    if "0"<=rs<="9":
        good[0]=True
    elif "A"<=rs<="Z":
        good[1]=True
    elif "a"<=rs<="z":
        good[2]=True
    elif rs in me:
        good[3]=True
res=0
if len(pa)>=8:
    res=1

res+=good.count(True)

print(res)