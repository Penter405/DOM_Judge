a,p,p,c=list(map(int,input().split()))
b1=[];b2=[]
for _ in range(a):
    b1.append(list(map(int,input().split())))

for _ in range(p):
    b2.append(list(map(int,input().split())))

new=[[0]*c for _ in range(a)]
for y in range(a):
    for x in range(c):
        now=0
        for index in range(p):
            now+=b1[y][index]*b2[index][x]
        new[y][x]=str(now)
for line in new:
    print(' '.join(line))