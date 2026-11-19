d=input()
stack=[]
result=0
index=0
int_buffer=[]
ints=[]
def clear(stack,ints,int_buffer):
    if len(int_buffer)!=0:
        ints.append(int("".join(int_buffer)))
        int_buffer.clear()
    for operator in stack[::-1]:
        if operator=="+":
            buffer=ints.pop()+ints.pop()
            ints.append(buffer)
        else:
            buffer=ints.pop()*ints.pop()
            ints.append(buffer)
    stack.clear()
    return ints.pop()
def recursion():
    global d,index
    buffer=[]
    stack=[]
    int_buffer=[]
    ints=[]
    while index<len(d):
        #when get into f(), make sure given index point to (
        try:
            now=int(d[index])
            int_buffer.append(str(now))
        except:
            now=d[index]
            if len(int_buffer)!=0:
                ints.append(int("".join(int_buffer)))
                int_buffer.clear()
            if now=="f":
                index+=2#now its ints
                a_int=recursion()#except recursion went ) and (
                ints.append(a_int)
            elif now==",":
                buffer.append(clear(stack,ints,int_buffer))
            elif now==")":
                buffer.append(clear(stack,ints,int_buffer))
                break
            elif now=="+" or len(stack)==0:
                stack.append(now)
            else:
                #now=="+"
                while len(stack)>0 and stack[-1]=="+":
                    pluser=ints.pop()+ints.pop()
                    ints.append(pluser)
                    stack.pop()
                
                stack.append("*")
        index+=1
    return max(buffer)-min(buffer)
while index<len(d):
    try:
        now=int(d[index])
        int_buffer.append(str(now))
    except:
        now=d[index]
        if len(int_buffer)!=0:
            ints.append(int("".join(int_buffer)))
            int_buffer.clear()
        if now=="f":
            index+=2#now its int
            a_int=recursion()#except recursion went ) and (
            ints.append(a_int)
        elif now=="+" or len(stack)==0:
            stack.append(now)
        else:
            #now=="*"
            while len(stack)>0 and stack[-1]=="+":
                pluser=ints.pop()+ints.pop()
                ints.append(pluser)
                stack.pop()
            
            stack.append("*")
    index+=1
print(clear(stack,ints,int_buffer))
