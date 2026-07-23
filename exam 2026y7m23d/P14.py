from collections import defaultdict
result=[]
times=defaultdict(int)
for _ in range(int(input())):
    man=input()
    if times[man]<2:
        result.append("GET")
        times[man]+=1
        continue
    else:
        result.append("FULL")
print("\n".join(result))