from itertools import permutations
data=input()
result=list(permutations(data))
to_str=[]
for rs in result:
    to_str.append(''.join(rs))
print('\n'.join(sorted(list(set(to_str)))))