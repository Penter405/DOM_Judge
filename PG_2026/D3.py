ys,xs,needx=list(map(int,input().split()))
longest=0
best=[-1,-1]
space_count=0
legal_lines=0

for boardy in range(1,ys+1):
    line=list(map(int,input().split()))
    sizeof=0
    this_line=False
    boardx=0
    pickx=0
    for d in line:
        boardx+=1
        if d:
            if sizeof!=0:
                if sizeof>longest:
                    best[0]=boardy
                    best[1]=pickx
                    longest=sizeof
            sizeof=0
        else:
            if sizeof==0:
                pickx=boardx
            space_count+=1
            sizeof+=1
            if this_line==False and sizeof>=needx:
                this_line=True
                legal_lines+=1
    if sizeof!=0:
        if sizeof>longest:
            best[0]=boardy
            best[1]=pickx
            longest=sizeof

print(space_count)
print(longest)
print(legal_lines)
if legal_lines>0:
    print(best[0],best[1])
else:
    print(-1,-1)