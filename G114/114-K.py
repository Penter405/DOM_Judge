get=[0]*26
get[ord("I")-65]=34
get[ord("O")-65]=35
get[ord("W")-65]=32
get[ord("Z")-65]=33
now=9
val=[0]*26
for rs in range(26):
    if get[rs]!=0:
        continue
    now+=1
    get[rs]=now
for rs in range(26):
    me=str(get[rs])
    val[rs]=int(me[0])+int(me[1])*9
s=input()
w=[8, 7, 6, 5, 4, 3, 2, 1, 1]
now=0
for rs in range(9):
    now+=int(s[rs])*w[rs]

res=[]
for rs in range(26):
    if (now+val[rs])%10==0:
        res.append(chr(65+rs))

print("".join(res))
