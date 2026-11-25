def solve():
    d=[]
    large=0
    for _ in range(int(input())):
        i=int(input())
        if i%10==0:
            large=max(large,i)
        else:
            large=max(large,i,int(str(i)[::-1]))
        d.append(i)
    prime=[False,False]+[True]*(large-1)
    for n in range(2,int(large**0.5)+2):
        if n<large and prime[n]:
            for bad in range(n*n,large+1,n):
                prime[bad]=False

    res=[]
    for want in d:
        if not prime[want]:
                    res.append(f'{want} is not a prime number.')
        elif want%10!=0 and prime[int(str(want)[::-1])] and int(str(want)[::-1])!=want:
            res.append(f'{want} is an emirp number.')
        else:
            res.append(f'{want} is a prime number.')

    print('\n'.join(res))
solve()