want=int(input())
if want==0:
    print(0)
    exit()
if want==1:
    print(1)
    exit()
a=0
b=1
for index in range(2,want+1):
    now=a+b
    a=b
    b=now
print(now%(10**9+7))