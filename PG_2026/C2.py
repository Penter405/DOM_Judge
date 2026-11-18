res=[]
for _ in range(int(input())):
    d=list(input())
    index=0
    while index<len(d):
        if d[index]=="a":
            d[index+1:len(d)]=d[len(d)-1:index:-1]
        elif d[index]=="b":
            d.extend(d[index+1:].copy())
        elif d[index]=="c":
            for more in range(1,3):
                index+=1
                if index>=len(d):
                    break
                d[index]=""
        index+=1
    print("".join(d))
