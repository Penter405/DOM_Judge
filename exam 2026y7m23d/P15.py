data=list(input())
result=[]
guy=input()
for rs in range(len(data)):
    data2=data.copy()
    data2.insert(rs,guy)
    result.append(''.join(data2))
data.append(guy)
result.append(''.join(data))
print('\n'.join(result))