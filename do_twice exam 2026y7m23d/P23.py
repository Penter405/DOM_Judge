result=None
s=input()
def is_letter(x):
    if 'A'<=str(x)<='Z' or 'a'<=str(x)<='z':
        return 1
    return 0
repeat=0
answer=[]
result=[]
ever=0
for rs in s:
    if is_letter(rs)==1:
        repeat+=1
        answer.append(rs)
    else:
        repeat=0
        
        answer=[]
    if repeat>ever:
        ever=repeat
        result=answer.copy()
if len(result)==0:
    print("None")
else:
    print(''.join(result))
"""
Hello!!! World123

"""