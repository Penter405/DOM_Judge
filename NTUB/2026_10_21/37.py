n=int(input())
if n==1:
    print(1)
elif n==2:
    print("1 1")
elif n==3:
    print("1 2 1")
else:
    now=[1,2,1]
    new=[]
    for _ in range(n-3):
        for rs in range(1,len(now)):
            new.append(now[rs]+now[rs-1])
        now=[1]+new+[1]
        new=[]
    now=list(map(str,now))
    print(" ".join(now))