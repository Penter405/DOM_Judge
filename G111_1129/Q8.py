from sys import stdin
"""
make sure only solution= theres no same value
"""


d=stdin.read().split("\n")
for line in d:
    if line=="":
        continue
    array,target=line.split()
    target=int(target)
    array=list(map(int,array.split(",")))
    #my_ind={array[rs]:rs for rs in range(len(array))}#if key same that value will be over write
    array=[(element,index) for index,element in enumerate(array.copy())]
    array.sort()
    left=0
    right=len(array)-1
    res=[0,0]
    while left<right:
        now=array[left][0]+array[right][0]
        if now==target:
            res[0]=array[left][1]
            res[1]=array[right][1]
            break
        if now<target:
            left+=1
        else:
            right-=1
    res.sort()
    print(res[0],res[1],sep=",")
