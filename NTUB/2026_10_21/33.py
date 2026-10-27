a=[]
b=[]
ab=[]
c=[]
abc=[]

ma,na=list(map(int,input().split()))
for _ in range(ma):
    a.append(list(map(int,input().split())))
mb,nb=list(map(int,input().split()))
for _ in range(mb):
    b.append(list(map(int,input().split())))
mc,nc=list(map(int,input().split()))
for _ in range(mc):
    c.append(list(map(int,input().split())))


#new_b=list(zip(*b))


for y in range(ma):
    buffer=[]
    for x in range(nb):
        b2=0
        for rs in range(mb):
            b2+=a[y][rs]*b[rs][x]
        buffer.append(b2)
    ab.append(buffer)

#ab = mz*nb
#new_c=list(zip(*c))
for y in range(ma):
    buffer=[]
    for x in range(nc):
        b2=0
        for rs in range(mc):
            b2+=ab[y][rs]*c[rs][x]
        buffer.append(b2)
    abc.append(buffer)


for y in abc:
    count=-1
    for x in y:
        count+=1
        if count!=0:
            print(" ",end="")
        print(x,end="")
    print("")
