t1=0
t2=0
t3=0
ever=set()
to_cheak=tuple([t1,t2,t3])
if to_cheak in ever:
    print("wrong")
else:   
    ever.add(to_cheak)

to_cheak=(t1,t2,t3)
if to_cheak in ever:
    print("wrong")
else:   
    ever.add(to_cheak)