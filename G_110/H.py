result=[]

    
"""def int16_to_10(x):
    result=0
    many_16=0
    for rs in str(x)[::-1]:
        many_16+=1
        result+=int(rs)*(16**many_16)

    return result

def reverse(x):
    if x==1:
        return 0
    return 1
def int10_to_2_with_reverse(x):
    result=[]
    while x>=1:
        bot=x//2
        x//=2
        result.append(reverse(bot))
    return result
def int2_to_16(x):
    result=[]
    for rs in range(0,len(x)-len(x)%4,4):
        bot=x[rs]+x[rs+1]*2+x[rs+2]*4+x[rs+3]*8
        if bot>9:
            result.append(chr(97+bot-10))
        else:
            result.append(str(bot))
    bot=0
    time=1
    for rs in x[len(x)-len(x)%4:]:
        bot+=rs*time
        time*=2
    if bot>9:
        result.append(chr(97+bot-10))
    else:
        result.append(str(bot))
    return result[::-1]
"""
"""
for _ in range(int(input())):
    add_tool=0
    buffer=input().replace(" ","")
    for rs in range(0, len(buffer)-1,2):
        add_tool+=int16_to_10(str(buffer[rs])+str(buffer[rs+1]))
    add_tool+=2
    to_be16=int10_to_2_with_reverse(add_tool)
    result.append(int2_to_16(to_be16)[20:24])
"""
for _ in range(int(input())):
    add_tool=0
    buffer=input().replace(" ","")
    

print(result)
