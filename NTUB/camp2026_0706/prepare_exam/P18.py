r=0
def to_list(x):
    return list(str(x).zfill(r))

def to_int(x):
    return int(''.join(x))

def get(n:int):
    global r
    result=0
    r=len(str(n))
    bot=to_list(n)
    no_different=1
    for rs in range(1,r):
        if bot[0]!=bot[rs]:
            no_different=0
    if no_different:
        return 0
    while True:
        result+=1
        n=to_list(n)
        n=to_int(sorted(n,reverse=True))-to_int(sorted(n,reverse=False))
        if (r==3 and n==495) or (r==4 and n==6174):
            return result
print(get(int(input())))