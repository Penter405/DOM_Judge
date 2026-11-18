def cheak(n):
    res=1
    if n%2==0:
        res+=1
    return res

for _ in range(int(input())):
    print(cheak(int(input())))