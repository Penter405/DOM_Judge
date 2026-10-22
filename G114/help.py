for n in range(10**9):
    get=[n]
    amount=1
    good=[]
    prime=[False,False]+[True]*(n+10)
    for rs in range(2,n+1):
        if prime[rs]:
            good.append(rs)
            for bad in range(rs*2,n+1,rs):
                prime[bad]=False