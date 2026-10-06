res=[]
while True:
    d=input()
    if d=="0":
        break
    sp,d=d.split()
    sp=len(d)//int(sp)
    ans=""

    for ind in range(0,len(d),sp):
        ans+=(d[ind:ind+sp])[::-1]
    
    res.append(ans)

print("\n".join(res))
"""
3 ABCEHSHSH
5 FAOETASINAHGRIONATWONOQAONARIO
0
"""