trans={
    "I":34,
    "O":35,
    "W":32,
    "Z":33
    }
i=10
n=65
while True:
    if i==32:
        break
    if chr(n) in trans:
        n+=1
        continue
    trans[chr(n)]=i
    n+=1
    i+=1
id=input()
i=9
buffer=0
for rs in id:
    i-=1
    i=max(i,1)
    buffer+=int(rs)*i

res=[]
for a,b in trans.items():
    im=str(b)
    im=int(im[0])+int(im[1])*9
    if (im+buffer)%10==0:
        res.append(a)
print("".join(sorted(res)))