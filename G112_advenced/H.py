import math
res=[]
for _ in range(int(input())):
    amount=int(input())
    ans=0
    d=list(map(int,input().split()))
    now=math.log2(d)
    if now != int(now):
        now=int(now)+1
    else:
        now=int(now)
    want_size=1
    for _ in range(now):
        want_size*=2
    d=[0]*want_size-len(d)+d
    #now sort binaryly
    #need increasing order
    my_range=2
    while True:
        for index in range(0,len(d),my_range):
            put_here=index
            did=0
            abegin=index
            bbegin=index+my_range//2
            aend=bbegin+1
            bend=index+my_range-1
            a=d[abegin:aend+1]
            b=d[bbegin:bend+1]
            pa=0
            pb=0
            while True:
                if pa==len(a):
                    while did<my_range:
                        d[put_here]=b[pb]
                        pb+=1;did+=1;put_here+=1
                        ans+=1
                    break
                elif pb==len(b):
                    while did<my_range:
                        d[put_here]=a[pa]
                        pa+=1;did+=1;put_here+=1
                        ans+=1
                    break
                if a[pa]<b[pb]:
                    d[put_here]=a[pa]
                    put_here+=1;pa+=1;did+=1
                    ans+=1
                else:
                    d[put_here]=b[pb]
                    put_here+=1;pa+=1;did+=1
                
                

        if my_range==len(d):
            break
        my_range*=2