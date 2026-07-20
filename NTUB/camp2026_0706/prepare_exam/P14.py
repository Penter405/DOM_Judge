from datetime import datetime
def get():
    place, sure=input().split(" ",1)
    sure=datetime.strptime(sure,"%Y/%m/%d %H:%M")
    hm=sure.strftime("%H:%M")
    if place=="Library":
        if datetime.strptime("2026/07/01 00:00","%Y/%m/%d %H:%M")<=sure<=datetime.strptime("2026/07/07 23:59","%Y/%m/%d %H:%M"):
            return 0
        if sure>datetime.strptime("2026/07/25 12:00","%Y/%m/%d %H:%M"):
            return 0
        if sure.weekday()==6:
            return 0
        elif sure.weekday()==5:
            if "10:00"<=hm<="17:00":
                return 1
            else:
                return 0
        else:
            if "09:00"<=hm<="20:00":
                return 1
            else:
                return 0
    else:
        me=[("2026/07/09 18:00", "2026/07/09 21:00"),("2026/07/10 22:00","2026/07/11 01:30"),("2026/07/17 18:00","2026/07/17 21:00"),("2026/07/24 22:00","2026/07/25 01:30")]
        anys=0
        for a,b in me:
            if datetime.strptime(a,"%Y/%m/%d %H:%M")<=sure<=datetime.strptime(b,"%Y/%m/%d %H:%M"):
                anys=1
                break
        return anys
        

result=[]
for rs in range(int(input())):
    if get()==1:
        result.append("YES")
    else:
        result.append("NO")
print('\n'.join(result))












#print(sure)
#help(datetime.strptime)


















"""result=[]
def get_day(x):
    #0=sumday
    #1=monday
    return x%7
def to_time(x,y):
    result=dict()
    bot=y.split(":")
    result["min"]=int(bot[1])
    result["hr"]=int(bot[0])
    bot=x.split("/")
    result["y"]=int(bot[0])
    result["m"]=int(bot[1])
    result["d"]=int(bot[2])
for _ in range(int(input())):
    s=input().split()
    if s[0]=="Library":
        now=to_time(s[1],s[2])
        
    else:
        now=to_time(s[1],s[2])
"""
