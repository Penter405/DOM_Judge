result=list()
depth=0
def recursion(now_depth:int,now:list,stack:list,buffer:str):
    global result,depth
    #print(f"now is {now_depth}, data is {now}, stack is {stack}")
    if buffer!="":
        #print(stack)
        if len(stack)==0:
            stack.append(buffer)
        elif buffer==")" and stack[-1]=="(":
            stack.pop(-1)
        else:
            stack.append(buffer)
        now.append(buffer)
    #print(stack)
    if  len(stack)!=0 and stack[-1]==")":
        return 0
    if now_depth==depth:
        #print(depth,"same as ",now_depth)
        #print(now, "will be join")
        if len(stack)==0:
            result.append("".join(now))
        return 0
    
    recursion(now_depth+1,now.copy(),stack.copy(),"(")
    recursion(now_depth+1,now.copy(),stack.copy(),")")
    

def get_result():
    global result,depth
    depth=int(input())*2
    recursion(0,list(),list(),"")
    #print(result)
    print("\n".join(result))
    #print("done")
get_result()