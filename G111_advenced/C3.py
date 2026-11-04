find=[]
while True:
    d=input().split()
    if d[0]=="0" and d[1]=="0":
        break
    if len(d[0])>len(d[1]):
        d[1]=d[1].zfill(len(d[0]))
    else:
        d[0]=d[0].zfill(len(d[1]))
    find.append((list(d[0][::-1]),list(d[1][::-1])))


for a,b in find:
    plus=0
    last=0
    for index in range(len(a)):
        now=int(a[index])+int(b[index])+last
        if now>=10:
            last=1
            plus+=1
        else:
            last=0
    if plus>1:
        print(f"{plus} carry operations.")
    elif plus==1:
        print(f"{plus} carry operation.")
    else:
        print("No carry operation.")