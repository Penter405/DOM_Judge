def get():
    result=set()
    n,k =list(map(int,input().split()))
    data=input()
    if n==k:
        return 1
    for rs in range(n-k+1):
        #print(data[0:rs]+data[rs+k:])
        result.add(data[0:rs]+data[rs+k:])
        
    
    return len(result)
result=[]
for _ in range(int(input())):
    result.append(str(get()))
print('\n'.join(result))