n=int(input())
last=None
keep=0
result=[]
for rs in input():
    if last==None:
        last=rs
        keep+=1
    else:
        if last==rs:
            keep+=1
        else:
            last=rs
            keep=1
    if keep>n:
        result.append(rs)
        
if len(result)==0:
    print("NONE")
else:
    print("".join(sorted(result)))