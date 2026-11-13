res=[]
while True:
    try:
        d=list(map(float,input().split()))
    except:
        break
    address=list();appear=dict()
    dam=None
    index=-1
    for rs in range(0,8,2):
        index+=1
        if (d[rs],d[rs+1]) in appear:
            dam=(d[rs],d[rs+1])
        address.append( [d[rs],d[rs+1]] )
        appear[(d[rs],d[rs+1])]=index
    appear.pop(dam)
    appear=list(appear.keys())
    res.append(    ( appear[0][0] +appear[1][0] -dam[0]  ,  appear[0][1] +appear[1][1] -dam[1] )   )


for a,b in res:
    a=int((a*1000))/1000
    b=int((b*1000))/1000
    print(f"{a:.3f} {b:.3f}")
"""
0.000 0.000 0.000 1.000 0.000 1.000 1.000 1.000
1.000 0.000 3.500 3.500 3.500 3.500 0.000 1.000
1.866 0.000 3.127 3.543 3.127 3.543 1.412 3.145
"""
"""
0.000 1.000 0.000 0.000 0.000 1.000 1.000 1.000
0.000 1.000 0.000 0.000 1.000 1.000 0.000 1.000
0.000 0.000 0.000 1.000 0.000 1.000 1.000 1.000
0.000 0.000 0.000 1.000 1.000 1.000 0.000 1.000
"""