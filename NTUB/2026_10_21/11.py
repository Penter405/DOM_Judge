d=input()
if d[0]=="-":
    nega=True
    d=d[1:]
else:
    nega=False
    if d[0]=="+":
        d=d[1:]
d=d.split(".")
now=str(int(d[0][::-1]))+"."+str(str(int(d[1]))[::-1])
if nega:
    print("-"+now)
else:
    print(now)
