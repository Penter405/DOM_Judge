import datetime

#help(datetime)

base=datetime.datetime.strptime("1970/01/01","%Y/%m/%d")
res=[]
for _ in range(int(input())):
    now=int(input())
    res.append( base+datetime.timedelta(days=now)  )
for rs in res:
    print(rs.year,str(rs.month).zfill(2),str(rs.day).zfill(2),sep="-")