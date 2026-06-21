from collections import defaultdict
walk=defaultdict(list)
find={}
for _ in range(int(input())-1):
    bot=list(map(int,input().split(",")))
    walk[bot[1]].append(bot[0])
    find[bot[0]]=bot[1]
buffer=[]
for _ in range(int(input())):
    buffer.append(int(input()))
for where in buffer:
    if where not in find:
        print(f"siblings {where} = ",end="")
        print("{}")
    else:
        bot=list(map(str,walk[find[where]]))
        bot.remove(str(where))
        print(f"siblings {where} = ",end="")
        if len(bot)==1:
            print("{",end="")
            print(f"{bot[0]}",end="")
            print("}")
        
        else:
            print("{",end="")
            print(f"{",".join(bot)}",end="")
            print("}")
        
#siblings 0 = {}