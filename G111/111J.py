#import time
#st=time.time()
n=int(input())
res=0
diff=1

for ind in range(len(bin(n+1)[2:])):
    res+= ((n+1)//(diff*2))*diff
    bot=(n+1)%(diff*2)  -diff
    if bot>0:
        res+=bot
    diff*=2
print(res)
#print(time.time()-st)

"""
o(n**2)

(  (int +1 ) // (diff*2)    )*diff  +   (  (int+1)%(diff*2) -diff )if >0

"""