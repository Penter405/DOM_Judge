a1,a2,b1,b2=list(map(int,input().split()))#1 =y    2=x
a=[]
b=[]
for _ in range(a1):
    a.append(list(map(int,input().split())))

for _ in range(b1):
    b.append(list(map(int,input().split())))

ab=[[0 for _ in range(a2*b2)] for _ in range(a1*b1)]

for ay in range(a1):
    for ax in range(a2):

        for by in range(b1):
            for bx in range(b2):
                ab[ay*b1+by][ax*b2+bx]=str(a[ay][ax]*b[by][bx])# 0 0 -> 0 , 1,1->5  


for ob in ab:
    print(" ".join(ob))
    