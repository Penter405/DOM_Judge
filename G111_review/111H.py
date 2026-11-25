from bisect import bisect_left
sizeof=int(input())
d=list(map(int,input().split()))
me=[]
for node in d:
    place=bisect_left(me,node)
    if place==len(me):
        me.append(node)
    else:
        me[place]=node
print(len(me))
