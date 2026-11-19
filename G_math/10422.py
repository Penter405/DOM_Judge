import math
result=[]
for _ in range(int(input())):
    d=list(map(int,input().split(",")))
    while len(d)!=1:
        d[-1]=math.gcd(d.pop(),d[-1])
    result.append(str(d[0]))
print("\n".join(result))