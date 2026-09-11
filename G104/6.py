#give up
"""
a=m*r  ,m=object=y
b=r*n  ,n=int=x


ab= at index[i][j]  times*rs for rs in a[i] all +b[j] all
ab=mn

m,r,r,n
"""

"""
s=[[1,2],[3,4],[5,6]]
print(list(zip(*s)))#index 1 0 to index 0 1
"""

aaaa=[]
n=int(input())
for _ in range(n):
    a=[]
    b=[]
    ab=[]
    ty=0
    tx=0
    a_or_b=-1
    m,r,r,n=list(map(int,input().split(',')))
    """
    if 9999 in a[ya]:
        ty=ya
        tx=a[ya].index(9999)
    """
    for ya in range(m):
        a.append(list(map(int,input().split())))
        if 9999 in a[ya]:
            ty=ya
            #tx=a[ya].index(9999)
            a_or_b=1
        
    for yb in range(r):
        b.append(list(map(int,input().split())))
        if 9999 in b[yb]:
            #ty=yb
            tx=b[yb].index(9999)
            a_or_b=2
    
    for yk in range(m):
        ab.append(list(map(int,input().split())))


    #try to get bot
    data=[]
    bad_index=-1
    bad_friend=-1
    good=0
    for rs in range(r):
        data.append((a[ty][rs],b[rs][tx]))
        if 9999 in data[-1]:
            if data[-1][0]==9999:
                bad_index=rs
                bad_friend=data[-1][1]
            elif data[-1][1]==9999:
                bad_index=rs
                bad_friend=data[-1][0]
        else:
            good+=a[ty][rs]*b[rs][tx]
    if bad_friend==0:
        bad_friend=1
    result=(ab[ty][tx]-good)//bad_friend
    aaaa.append(str(result))


print('\n'.join(aaaa))


"""
2
2,3,3,4
1 2 9999
0 -4 1
3 1 0 2
-1 2 5 0
0 -2 2 1
1 -1 16 5
4 -10 -18 1
4,3,3,5
2 4 1
3 6 2
2 5 0
1 2 3
2 6 2 0 2
3 1 1 1 2
9999 2 2 0 1
20 18 10 4 13
32 28 16 6 20
19 17 9 5 14
20 14 10 2 9 
"""

    