from collections import Counter
u=input()
d=list(map(int,input().split()))
d=list(dict(Counter(d)).items())
d.sort()
for num,time in d:
    print(num,time)




