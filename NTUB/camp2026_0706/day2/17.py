import math
def recursion(a:int,b:int,times=0):
    if b<=0:
        return times
    return recursion(b,pow(a,1,b),times+1)
result=[]
for _ in range(int(input())):
    a,b=input().split()
    a=int(a)
    b=int(b)
    result.append([])
    result[-1].append(str(math.gcd(a,b)))
    result[-1].append(str(recursion(a,b)))
for rs in result:
    print(" ".join(rs))
