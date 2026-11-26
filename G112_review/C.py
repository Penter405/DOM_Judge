d=int(input())
d+=1911
if d%4!=0:
    print(False)
elif d%4==0 and d%100!=0:
    print(True)
elif d%100==0 and d%400!=0:
    print(False)
elif d%400==0:
    print(True)
