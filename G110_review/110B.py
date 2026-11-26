for _ in range(int(input())):
    d=int(input())
    if d%4!=0:
        print('a normal year')
    elif d%4==0 and d%100!=0:
        print("a leap year")
    elif d%100==0 and d%400!=0:
        print('a normal year')
    else:
        print('a leap year')

        
    