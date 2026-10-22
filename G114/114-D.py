res=[]
for _ in range(int(input())):
    a,b=list(map(int,input().split()))
    if a%2==0:
        a+=1
    if b%2==0:
        b-=1
    res.append(int(  (a+b)/2*(((b-a)+2)//2)))
for rs in res:
    print(rs)