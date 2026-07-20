n=int(input())
def do(n):
    for index in range(n,0,-1):
        buffer=0
        for may_child in range(1,index+1):
            if index%may_child==0:
                buffer+=may_child
        if buffer==n:
            return index
    return 0
print(do(n))