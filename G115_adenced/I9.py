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
res=str(trans[id[0]])
res=int(res[0])+int(res[1])*9
i=9
for rs in id[1:]:
    i-=1
    i=max(i,1)
    res+=int(rs)*i

if res%10==0:
    print("Y")
else:
    print("N")