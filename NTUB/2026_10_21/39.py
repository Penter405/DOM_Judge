def get():
    used=set()
    n=int(input())
    times=-1
    appeared={
        str(n):0
        }
    count=0
    ever=False    
    new=n
    times=0
    last=None
    while True:
        times+=1
        buffer=0
        for rs in str(new):
            buffer+=(int(rs))**2
        new=buffer
        
        if new in appeared:
            if last!=None:
                if appeared[new]-1!=appeared[last] or new in used:
                    return count
                
            last=new
            used.add(new)
            count+=1
        else:
            appeared[new]=times
        #print("log", new)


res=[]
for _ in range(int(input())):
    res.append(str(get()))
print("\n".join(res))