from bisect import bisect_left
amount=int(input())
d=list(map(int,input().split()))
me=[]
for index in range(len(d)):
    place=bisect_left(me,d[index])
    if place>=len(me):
        me.append(d[index])
    else:
        me[place]=d[index]
print(len(me))