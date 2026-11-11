index=int(input())
res=[]
if index<=2500:
    res.append(str(1))
    res.append(str( ((index-1)//25)+1 ))
    index-=(index-1)//25 *25
    res.append(str(index))
elif index <= 7500:
    res.append(str(2))
    index-=2500
    res.append(str( ((index-1)//50)+1 ))
    index-=(index-1)//50 *50
    res.append(str(index))
else:
    res.append(str(3))
    index-=7500
    res.append(str( ((index-1)//25)+1 ))
    index-=(index-1)//25 *25
    res.append(str(index))

print(" ".join(res))