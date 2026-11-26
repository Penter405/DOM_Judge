for _ in range(int(input())):
    d=input()
    if len(d)==5:
        print(3)
    else:
        now=[1 for a,b in zip(d,'one') if a==b]
        if len(now)>=2:
            print(1)
        else:
            print(2)