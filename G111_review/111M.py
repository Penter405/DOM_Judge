from collections import Counter
sizeof=int(input())
d=list(map(int,input().split()))
res=list(Counter(d).most_common())
res.sort(key= lambda x:x[0])
for a,b in res:
    print(a,b)