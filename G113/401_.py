m, n,n ,p=list(map(int,input().split()))
a=[]
b=[]
for _ in range(m):
    a.append(list(map(int,input().split())))

for _ in range(n):
    b.append(list(map(int,input().split())))

ab=[]
b=list(zip( *b ))

for rs in range(m):
    bot=[]
    for pe in range(p):
        buffer=0
        for i in range(n):
            buffer+=a[rs][i]*b[pe][i]
        bot.append(str(buffer))
    ab.append(bot)


for rs in ab:
    print(" ".join(rs))