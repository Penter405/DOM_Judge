get=[0]*26
get[ord("I")-ord("A")]=34
get[ord("O")-ord("A")]=35
get[ord("W")-ord("A")]=32
get[ord("Z")-ord("A")]=33
now=9
for rs in range(26):
    if get[rs]==0:
        now+=1
        get[rs]=now
def legal():
    time=9
    id=input()
    if id[0]>"Z" or id[0]<"A":
        return False

    if id[1]!="1" and id[1]!="2":
        return False
    

    count=str(get[ord(id[0])-ord("A")])
    count=int(count[0])+int(count[1])*9
    for rs in id[1:]:
        if rs>"9" and rs<"0":
            return False
        time-=1
        if time<1:
            time=1
        count+=time*int(rs)

    if count%10==0:
        return True
    else:
        return False

if legal():
    print(1)
else:
    print(0)
