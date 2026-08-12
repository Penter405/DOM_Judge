num ,ori, to=input().split()
ori=int(ori)
to=int(to)
new=int(num,ori)

def get(x,cut):
    result=[]
    while(x>0):
        result.append(str(x%cut))
        x//=cut
    return "".join(result[::-1])
print(get(new,to))