out=[]
def add(guy):
    while guy<=size:
        bit[guy]+=1
        guy+=guy&-guy
def find(guy):
    res=0
    while guy>0:
        res+=bit[guy]
        guy-=guy&-guy
    return res



while True:
    try:
        size,time=list(map(int,input().split()))
    except:
        break
    res=[]
    array=[0]+[n for n in range(size,0,-1)]
    my_index=[0]+[size+1-n for n in range(1,size+1)]
    for _ in range(time):
        a,b=list(map(int,input().split()))
        my_name=[]
        my_value=0
        #edit array first---wrong
        aind=my_index[a]
        bind=my_index[b]
        array[aind],array[bind]=array[bind],array[aind]
        my_index[a],my_index[b]=my_index[b],my_index[a]
        count=0
        #get someone's smaller
        bit=[0]*(size+1)
        for index in range(1,size+1):
            now_name=array[index]
            now_value=find(now_name)
            if a==b:
                count+=now_value
            if now_value>my_value:
                my_name=[now_name]
                my_value=now_value
            elif now_value==my_value:
                my_name.append(now_name)
            #still need to update
            add(now_name)


        if a==b:
            res.append(str(count))
        else:
            res.append(f"{min(my_name)}:{my_value}")
    out.append("\n".join(res))

print("\n----------\n".join(out))