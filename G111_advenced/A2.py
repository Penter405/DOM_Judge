x=int(input())
y=int(input())
if x>y:
    x,y=y,x
for rs in range(x+1,y):
    if rs%5==2 or rs%5==3:
        print(rs)