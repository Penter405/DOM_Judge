from datetime import datetime
inside=[
("2026/06/22 13:30","2026/06/22 16:00"),
("2026/06/23 10:30","2026/06/23 12:00"),
("2026/06/24 10:30","2026/06/24 12:00"),
("2026/06/24 13:30","2026/06/24 16:00"),
("2026/06/25 10:30","2026/06/25 12:00"),
("2026/06/25 13:30","2026/06/25 16:00"),
("2026/06/26 10:30","2026/06/26 12:00"),
("2026/06/26 13:30","2026/06/26 16:00")
]

def get():
    place=input()
    data=input()
    date=datetime.strptime(data,"%Y/%m/%d %H:%M")
    if place=="Taipei":
        if '12:00'<=date.strftime("%H:%M")<='13:00':
            return 0
        t1='2026/06/17 09:00'
        t2='2026/06/24 17:00'
        if datetime.strptime(t1,"%Y/%m/%d %H:%M")<=date<=datetime.strptime(t2,"%Y/%m/%d %H:%M"):
            return 1
    else:
        for a,b in inside:
            if datetime.strptime(a,"%Y/%m/%d %H:%M")<=date<=datetime.strptime(b,"%Y/%m/%d %H:%M"):
                return 1
        return 0
if get()==1:
    print("YES")
else:
    print("NO")