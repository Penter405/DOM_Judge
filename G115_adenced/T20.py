import sys
d=sys.stdin.read()
res=[]
res.append(str(d.count("\n")))
d2=d
d2=d2.replace("\n"," ").replace("\t"," ")
res.append(str(len(d2.split())))
res.append(str(len(d)))
print(" ".join(res))