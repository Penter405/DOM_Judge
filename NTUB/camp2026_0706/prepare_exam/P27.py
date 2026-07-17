from itertools import combinations
s=input()
s=s.replace(" ",'')
s=list(map(int,s.split(',')))
get_2=combinations(s,3)
result=set()
for rs in get_2:
    result.add(sum(rs))
print(len(result))