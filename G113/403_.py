
id=input()
get=dict()
get["I"]=34
get["O"]=35
get["W"]=32
get["Z"]=33

bot=9
rs=64
for _ in range(26):
    rs+=1
    if chr(rs) in get:
        continue
    bot+=1
    #print(chr(rs),bot)
    get[chr(rs)]=bot


now=str(get[id[0]])
now=int(now[0])+int(now[1])*9
bot=9
for rs in id[1:]:
    bot-=1
    if bot<1:
        bot=1
    now+=bot*int(rs)

if now%10==0:
    print("Y")
else:
    print("N")
