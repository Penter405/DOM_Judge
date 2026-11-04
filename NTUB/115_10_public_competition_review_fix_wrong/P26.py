r=dict()
for _ in range(int(input())):
    me,word,root,_=input().split(",")
    me=int(me)
    root=int(root)
    if me==root:
        r[me]=[word,[]]
    else:
        r[root][1].append([me,word])
gind=0
for root in sorted(list(r.keys())):
    gind+=1
    print(gind,r[root][0],sep=".")
    index=0
    for cind,child in sorted(r[root][1]):
        index+=1
        print(f"**{gind}-{index}.{child}")

