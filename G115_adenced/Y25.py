d=int(input())
res=[]
res.append(str(d//3600))
d=d-(d//3600)*3600
res.append(str(d//60))
d=d-(d//60)*60
res.append(str(d))
print(" ".join(res))