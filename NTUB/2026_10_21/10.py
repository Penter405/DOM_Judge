ed=[1,1]
n=int(input())
for rs in range(1,n+1):
    if rs==1:
        print("1")
        continue
    if rs==2:
        print("1 1")
        continue
    now=[1]
    for pe in range(rs-2):
        now.append(ed[pe]+ed[pe+1])
    now.append(1)
    print(" ".join(list(map(str,now))))
    ed=now.copy()
