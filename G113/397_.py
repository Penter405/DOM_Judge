a,b=list(map(int,input().split()))
if b<a:
    a,b=b,a
if a%2!=0:
    a+=1
if b%2!=0:
    b-=1
print( (a+b)//2*( (b-a)//2+1 ) )
