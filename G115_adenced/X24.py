def imnot(d):
    res=[]
    for rs in d:
        if rs=="1":
            res.append("0")
        else:
            res.append("1")
    return "".join(res)
res=[]
for _ in range(int(input())):
    d=input().split()
    bnum=0
    for rs in range(0,len(d),2):
        hex_num=d[rs]+d[rs+1]
        num=int(hex_num,16)
        bnum+=num
    bnum=hex(bnum)[2:]
    if len(bnum)==5:
        bnum=int(bnum[1:],16)+int(bnum[0],16)
    else:
        bnum=int(bnum,16)
    rnum=imnot(bin(bnum)[2:].zfill(16))
    res.append(hex(int(rnum,2))[2:])

for rs in res:
    if len(rs)<4:
        print("0"*(4-len(rs)),end="")
    print(rs)
"""

5
45 00 00 30 cc 61 40 00 40 06 00 00 0a 05 04 6b 0a 08 09 ed
45 00 00 73 00 00 40 00 40 11 b8 61 c0 a8 00 01 c0 a8 00 c7
45 00 00 47 73 88 40 00 40 06 00 00 83 9f 0e 85 83 9f 0e a1
45 00 00 47 73 88 40 00 40 06 a2 c4 83 9f 0e 85 83 9f 0e a1
45 00 05 14 42 a2 21 40 80 01 00 00 c0 a8 00 03 c0 a8 00 01
"""
"""

4
45 00 00 47 73 88 40 00 40 06 00 00 83 9f 0e 85 83 9f 0e a1
45 00 00 47 73 88 40 00 40 06 a2 c4 83 9f 0e 85 83 9f 0e a1
45 00 00 30 cc 61 40 00 40 06 00 00 0a 05 04 6b 0a 08 09 ed
45 00 05 14 42 a2 21 40 80 01 00 00 c0 a8 00 03 c0 a8 00 01
"""