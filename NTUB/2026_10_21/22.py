a=[]
m,p=list(map(int,input().split()))
for _ in range(m):
    a.append(list(map(int,input().split())))
b=[]
p,n=list(map(int,input().split()))
for _ in range(p):
    b.append(list(map(int,input().split())))

b=list(zip(*b))
ab=[[0 for _ in range(n)] for _ in range(m)]

for rs in range(m):
    for pe in range(n):
        bot=0
        for i in range(p):
            bot+=a[rs][i]*b[pe][i]
        ab[rs][pe]=(bot)
res=str(ab)
res=res.replace(" ","")
print(res)

"""
3 1
1
-1
2
1 2
3 4
"""