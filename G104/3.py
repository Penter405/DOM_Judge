from itertools import permutations
"""
i=int 123456
j=want 
k=want
"""
result=[]
for _ in range(int(input())):
    data=list(map(int,input().split(',')))
    got=sorted(list(permutations(str(data[0]),len(str(data[0])))))
    
    result.append(str(int("".join(got[data[1]-1]))+int("".join(got[data[2]-1]))))


print('\n'.join(result))

