result=[]
for _ in range(int(input())):
    data=input().split()
    plus=0
    for rs in range(0,len(data),2):
        plus+=int(data[rs]+data[rs+1],16)

    got=hex(plus)[2:]
    if len(got)%4!=0:
        got="0"*(4-len(got)%4)+got
    buffer=0
    for rs in range(0,len(got),4):
        buffer+=int(got[rs:rs+4],16)

    got=bin(buffer)[2:].zfill(16)
    new=[]
    for rs in got:
        if rs=="0":
            new.append("1")
        else:
            new.append("0")
    
    result.append(    hex(int("".join(new),2))[2:].zfill(4)    )


print("\n".join(result))
    
    
