res=[]

def recur(me):
    res.append(str(me))
    if me==1:
        return 0
    if me%2==0:
        recur(me//2)
    else:
        recur(me*3+1)

recur(int(input()))

print(" ".join(res))