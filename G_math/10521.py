for _ in range(int(input())):
    a,b=input().split("/")
    a=list(map(int,a.split(".")))
    b=list(map(int,b.split(".")))
    new=[]
    for index in range(4):
        new.append(str(a[index]&b[index]))
    print(".".join(new))