

def get():
    total=0
    b=int(input())
    prime=[1]*(b+1)
    prime[0]=0
    prime[1]=0
    for index in range(b+1):
        if prime[index]:
            if b%index==0:
                total+=index
            for do in range(index**2,b+1,index):
                prime[do]=0
    return int(b%total==0)
print(get())