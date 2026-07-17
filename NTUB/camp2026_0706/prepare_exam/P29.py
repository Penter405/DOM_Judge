import math
from collections import defaultdict
s=input()
times=defaultdict(int)
#print(unique)
result=math.factorial(len(s))
for rs in s:
    times[rs]+=1
for rs in times.values():
    result/=math.factorial(rs)
print(int(result))