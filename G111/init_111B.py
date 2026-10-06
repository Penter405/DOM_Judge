table=[0,0]+[1]*(10**6-1)
prime=[]
for rs in range(10**6+1):
    if table[rs]==1:
        prime.append(rs)
        for pe in range(rs**2,10**6+1,rs):
            table[pe]=0

with open("DOM_Judge/G111/init_111B.txt", "w") as f:
    f.write(f"prime={prime}")