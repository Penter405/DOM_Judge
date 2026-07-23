from collections import Counter
data=input().split()
data=data[1:]
data2=input().split()
data.extend(data2[1:])
result=[]

for ele, times in Counter(data).most_common():
    if times>=2:
        result.append(ele)
if len(result)>0:
    print(" ".join(sorted(result)))
else:
    print("NONE")