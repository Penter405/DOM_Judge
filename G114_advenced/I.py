data=[]
for _ in range(int(input())):
    data.append(int(input()))

large=max(data)

factor=[0 for _ in range(large+1)]#skip index 0
#fdebug=[[] for _ in range(large+1)]
prime=[-1,-1]+[0]*(large+1)
#pdebug=[[] for _ in range(large+1)]
for partner in range(1,large+1):
    #factor first
    for go_through in range(partner,large+1,partner):
        factor[go_through]+=1
        #fdebug[go_through].append(partner)
    #and then prime amount
    if prime[partner]==0:
        for go in range(partner,large+1,partner):
            prime[go]+=1
            #pdebug[go].append(partner)

for guy in data:
    print(factor[guy]-prime[guy])
    

