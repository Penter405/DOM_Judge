res=[]
def get(i):
    if i==0:
        return "0.00"
    if i<0:
        nega=True
    else:
        nega=False
    poi=abs(i)
    d=str(i).split(".")
    if len(d[1])>=3:
        if int(d[1][2])>=5:
            bot=str((float(f"{d[0]}.{d[1][:2]}")+0.01))
        else:
            bot=str(float(f"{d[0]}.{d[1][:2]}"))
    else:
        bot=str(i)
    if float(bot)==0:
        return "0.00"
    if nega:
        return bot
    return bot
for _ in range(int(input())):
    res.append(get(float(input())))
    

for rs in res:
    print(f"{float(rs):.2f}")
"""
10
1.00000
0.5
0.715
0.1234567890
-0.995
0.315
0.316
0.415
0.416
-0.00325
"""