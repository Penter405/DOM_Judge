l,r,k=list(map(int,input().split()))
fun="! @ # $ % ^ & * ( ) _ - + ="
fun.replace(" ","")
fun=set(fun)
def legal():
    global l,r,k
    #legal=0

    any_big=0
    any_small=0
    any_int=0
    any_fun=0
    last=None
    repeat=0
    k_bad=0
    data=input()
    if not (l<=len(data)<=r):
        return 1
    for rs in data:
        try:
            rs=int(rs)
            any_int=1
        except:
            if rs in fun:
                any_fun=1
            elif rs==rs.upper():
                any_big=1
            elif rs==rs.lower():
                any_small=1
        if last==None or last==rs:
            repeat+=1
        elif last!=rs:
            repeat==1
        last=rs
        if repeat>k:
            k_bad=1
    if any_big==0:
        return 2
    elif any_small==0:
        return 3
    elif any_int==0:
        return 4
    elif any_fun==0:
        return 5
    elif k_bad==1:
        return 6
    #for rs in range(len(data)):
    #    for pe in range(rs+1,len(data)+1):
            


    return 0


result=legal()
if result==0:
    print("Valid")
else:
    print(result)
"""
1 10 3
B1!aaaa
"""