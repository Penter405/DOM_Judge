a,b=list(map(int,input().split()))
result=0
def adds(x):
    global result
    if a <= x <b:
        result+= 1
        

prime=[1]*(b+1)
prime[0]=0
prime[1]=0
for index in range(b+1):
    if prime[index]:
        adds(index)
        for do in range(index**2,b+1,index):
            prime[do]=0

print(result)
