result=0
n=int(input())
way=[]
while True:
    if n==6174:
        break
    result+=1
    n=list(str(n))
    big=''.join(sorted(n))
    small=''.join(sorted(n)[::-1])
    n=int(small)-int(big)
    way.append(f"{small} - {big} = {n}")
print('\n'.join(way))
print(result)