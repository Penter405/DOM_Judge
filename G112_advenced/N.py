import datetime
res=[]
date=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
for _ in range(int(input())):
    m,d=list(map(int,input().split()))
    t=datetime.datetime(2023,m,d)

    res.append(date[t.weekday()])


for rs in res:
    print(rs)
"""
9
1 6
2 28
4 5
5 26
8 1
11 1
12 25
12 31
3 9

"""