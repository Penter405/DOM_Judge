first=True
n=int(input())
child=1
child2=1
for rs in range(n):
    if rs!=0:
        print(",",end="")
    if rs==0:
        print("1",end="")
    elif rs==1:
        print("1",end="")
    else:
        now=child+child2
        print(now,end="")
        child=child2
        child2=now