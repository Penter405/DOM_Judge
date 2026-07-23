from datetime import datetime
data="2026/03/19 12:20"
d=datetime.strptime(data,"%Y/%m/%d %H:%M")
print(d.weekday())
print(d)


data=list(map(int,input().split()))