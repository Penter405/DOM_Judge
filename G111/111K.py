want=[]
res=[]
large=0
for _ in range(int(input())):
    want.append(list(map(int,input().split())))
    if want[-1][1]>large:
        large=want[-1][1]
    res.append([])

table=[0,0]+[1]*(large-1)

for rs in range(large+1):
    if table[rs]==1:
        
        for pe in range(rs**2,large+1,rs):
            table[pe]=0
        index=-1
        for guy,back in want:
            index+=1
            if guy<=rs<=back:
                res[index].append(str(rs))

new=[]
for rs in res:
    new.append("\n".join(rs))

#print(new)
print("\n\n".join(new))
"""
3
1 10
3 5
1000000 1000090
"""