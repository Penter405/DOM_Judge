"""def get():
    result=set()
    data=input()
    size=len(data)
    front=dict()#new front used => bad
    front['c']='d'
    front['c']
    limit=[data.count('d'),data.count('r'),data.count('c')]
    def recursion(pointer=0,out="",used=[]):
        if pointer==size:
            result.add(out)
        
        for rs in range(3):
            if used[rs]!=limit[rs]:
                
    return len(result)
    recursion(used=[0]*3)
print(get())
"""
# dc  rc
import math
s=input()
chiken=0
dog=0
rabbit=0
for rs in s:
    if rs=='c':
        chiken+=1
    elif rs=='d':
        dog+=1
    else:
        rabbit+=1
print(int(math.factorial(dog+rabbit)/(math.factorial(dog)*math.factorial(rabbit))))