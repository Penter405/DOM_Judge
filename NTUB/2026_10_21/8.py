n1=int(input())
n2=int(input())
def legal(n):
    for rs in str(n):
        if rs=="0":
            return False
        if n%int(rs)!=0:
            return False

    return True

count=0
for rs in range(n1,n2+1):
    if legal(rs):
        count+=1

print(count)