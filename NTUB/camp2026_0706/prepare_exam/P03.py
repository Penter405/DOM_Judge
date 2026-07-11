def get():
    n,k=input().split()
    n=int(n)
    k=int(k)
    n+=1
    while True:
        if n%k==0:
            return n
        n+=1
print(get())