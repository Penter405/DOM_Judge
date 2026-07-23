result=0
n=int(input())
while True:
    if n==6174:
        break
    result+=1
    n=list(str(n))
    big=''.join(sorted(n))
    small=''.join(sorted(n)[::-1])
    n=int(small)-int(big)
print(result)