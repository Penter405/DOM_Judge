result=[]
#data=[str(bot).zfill(2)+":00 AM" for bot in range(1,12)]
for _ in range(int(input())):
    s=input()
    s2=s.split()
    time=s2[0].split(":")
    time.append(s2[1])
    if time[0]=="12":
        time[0]="00"
    if (time[2]=="AM"):   
        result.append(s2[0])
    else:
        time[0]=(str(int(time[0])+12)).zfill(2)
        result.append(time[0]+":"+time[1])
        
print("\n".join(result))