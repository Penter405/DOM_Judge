for _ in range(int(input())):
    d=input().replace('X',' ')
    d=d.split()
    res=0
    for chars in d:
        res+=(1+len(chars))*len(chars)//2
    print(res)