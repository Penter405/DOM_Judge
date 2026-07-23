from itertools import permutations
data=input()
out=set(permutations(data))
result=0
#print(out)
for rs in out:
    rs=''.join(rs)
    if "TW" in rs or "BC" in rs:
        continue
    else:
        result+=1
print(result)