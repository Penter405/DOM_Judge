from datetime import datetime
#print(help(datetime))

def make_date(d:str):
    
    return datetime(y,m,d)
res=[]
for _ in range(int(input())):
    d,m,y=list(map(int,input().split("/")))
    d2,m2,y2=list(map(int,input().split("/")))
    if m>m2 or (m==m2 and d>=d2):
        res.append(y-y2)
    else:
        res.append(y-y2-1)
for rs in res:
    print(rs)