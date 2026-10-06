res=[[],["0","1"]]
n=int(input())
for rs in range(2,n+1):
    res.append([])
    for pe in res[-2]:
        res[-1].append("0"+pe)
    for pe in res[-2][::-1]:
        res[-1].append("1"+pe)
print("\n".join(res[-1]))
"""
0 + list
1+ reversed list
"""