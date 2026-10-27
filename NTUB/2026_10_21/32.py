res=[0,0]
def get():
    """
    math prove:
        every 2 4 6 is not result, if element 2 is not in range l to r+1
        the best answer will only be separate by integer 2 4 6, which is only 1 integer on their middle
        if range include 2, and 3-> return 1
        else -> best=2

    
    
    """
    intcount=float("inf")
    l,r=list(map(int,input().split()))
    if l<=2 and r>=3:
        res[0]=2
        res[1]=3
        return 1

    prime=[False,False]+[True]*(int(r**0.5)+1)
    #intenger=l+index of num
    num=[n for n in range(l,r+1)]
    
    for n in range(2,len(prime)):
        if prime[n]:
            for rs in range(n*2,len(prime),n):
                prime[rs]=False
            prime_last=None
            last=None
            more_last=None
            intcount=float("inf")
            for ind in range(len(num)):
                if num[ind]!=-1 and num[ind]%n==0:
                    num[ind]=1
                if num[ind]!=1 and num[ind]!=-1:
                    if prime_last!=None:
                        if ind+l-prime_last<intcount:
                            intcount=ind+l-prime_last
                            res[0]=prime_last
                            res[1]=ind+l
                            if intcount==2:
                                return res
                    prime_last=ind+l

                if num[ind]!=1:
                    if last!=None and more_last!=None:
                        if ind-last>intcount and last-more_last>intcount:
                            num[last]=-1#would be prime but it is not answer
                    more_last=last
                    last=ind
    
get() 
"""
last=None
intcount=float("inf")
res=[0,0]        
for ind in range(len(num)):
    if ind+l==num[ind]:
        if last!=None and ind+l-last<intcount:
            res=[last,ind+l]
            intcount=ind+l-last
            if intcount==1:
                break
        last=ind+l

"""


if res.count(0)!=2:
    print(res[0],res[1])
else:
    print(-1)