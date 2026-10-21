d=input().split()
pre=[]
ino=[]
post=[]

def recursion(n):
    if n>len(d)-1:
        return 0
    if d[n]=="null":
        return 0
    pre.append(d[n])

    recursion(n*2+1)

    ino.append(d[n])

    recursion(n*2+2)

    post.append(d[n])
    return 0

recursion(0)
print(" ".join(pre))
print(" ".join(ino))
print(" ".join(post))
"""
M N K I J L Y A H G F E D null null null null null null B C
"""