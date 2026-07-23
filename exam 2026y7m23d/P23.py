result=None
s=input()
last=None
def is_letter(x):
    if 'A'<=str(x)<='Z' or 'a'<=str(x)<='z':
        return 1
    return 0
repeat=0
answer=[]
ever=0
for rs in s:
    if is_letter(rs)==1:
        repeat+=1
        answer.append(rs)
    else:
        repeat=0
    if repeat>ever:
        ever=repeat
print(ever)