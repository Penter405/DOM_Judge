def get():
    t=int(input())
    t+=1911
    if t%4!=0:
        return False
    elif t%4==0 and t%100!=0:
        return True
    elif t%100==0 and t%400!=0:
        return False
    elif t%400==0:
        return True

print(get())
