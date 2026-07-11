result=0
me=int(input())
while True:
    if me==0:
        break
    member=list(map(int,list(str(me))))
    me-=max(member)
    result+=1
print(result)