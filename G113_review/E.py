from collections import Counter
sizeof=int(input())
d=list(map(int,input().split()))
good=[]
value=0
for k,v in Counter(d).most_common():
    if v>value:
        good=[k]
        value=v
    elif v==value:
        good.append(k)
for guy in sorted(good):
    print(guy,value)