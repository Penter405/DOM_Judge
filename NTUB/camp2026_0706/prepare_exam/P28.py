data=list(map(int,input().split(", ")))
large=sum(data)
result=large
def more_0(x):
    if x<0:
        return -x
    return x
def recursion(pointer=0,plus=0,path_best=large+1):
    global result, diff
    if more_0(large-plus*2)<result:
        result=more_0(large-plus*2)
    if pointer==len(data):
        return 0
    if more_0(large-plus*2)>path_best:
        return 0
    for rs in (data[pointer],0):
        recursion(pointer+1,plus+rs,more_0(large-plus*2))
recursion()
print(result)