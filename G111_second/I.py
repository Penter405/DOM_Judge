res=[]
for _ in range(int(input())):
    d=input()
    ind=0
    bu=0
    for rs in d[::-1]:
        bu+=(ord(rs)-64)*(26**ind)
        ind+=1
    res.append(str(bu))

for rs in res:
    print(rs)

"""
3
A
AZ
AAA
"""