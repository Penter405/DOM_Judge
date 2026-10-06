result=[]

for _ in range(int(input())):

    #index 10,11
    data=input().split()
    plused=0
    for rs in range(0,len(data),2):
        plused+=int(data[rs]+data[rs+1],16)
    hexed=hex(plused)
    hexed=hexed[2:]
    if len(hexed)%4!=0:
        hexed="0"*(4-len(hexed)%4)+hexed
    plused=0
    for rs in range(0,len(hexed),4):
        #print(hexed[rs:rs+4])
        plused+=int(hexed[rs:rs+4],16)
    #print(hex(plused))
    ans=[]
    bot=bin(plused)[2:].zfill(16)#here is the probelm
    for rs in bot:
        if rs=="0":
            c="1"
        else:
            c="0"
        ans.append(c)
    result.append(hex(int("".join(ans),2))[2:].zfill(4))
print("\n".join(result))
#https://chatgpt.com/share/6ac4894b-6118-83ee-87d6-5de8175019fd