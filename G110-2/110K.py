result=[]
count=-1
while True:
    count+=1
    try:
        if count!=0:
            bot=input()
        a=int(input())
        b=int(input())
        c=int(input())
    except:
        break
    result.append(str(pow(a,b,c)))
print("\n".join(result))
"""
65535
65535
36123

2374859
3029382
36123

"""