events=int(input())
d=[]
large=0
for _ in range(events):
    a,b=list(map(int,input().split()))
    d.append([a,b])
    large=max(large,a,b)
    

d.sort()
premax=[0]
value=[0]
for start,end in d:
    best_value=0
    for index in range(len(premax)):
        if premax[index]>start:
            continue

        if value[index]>best_value:
            best_value=value[index]
    premax.append(end)
    value.append(best_value+1)

print(max(value))