from sys import stdin
res=[]
d=stdin.read().split("\n")[:-1]
for line in d:
    array=list(map(int,line.split()))
    allow_max,array=array[0],array[1:]
    allow_max-=1
    last=None
    good=True
    for data in array:
        if last!=None:
            if 1<=abs(last-data)<=allow_max:
                pass
            else:
                good=False

        last=data
    res.append(good)

for line in res:
    if line:
        print("Jolly")
    else:
        print("Not jolly")