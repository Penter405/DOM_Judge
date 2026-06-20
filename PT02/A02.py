result=[]
walked=set()
useless=input()
coin=list(map(int,input().split()))
question=int(input())
def recursion(used,total):
    #print(used)
    if total>question:
        return 0
    if tuple(used) in walked:
        return 0
    walked.add(tuple(used))
    if total==question:
        result.append(tuple(used))
        return 0
    
    for rs in range(len(used)):
        uses=used.copy()
        uses[rs]+=1
        recursion(uses,total+coin[rs])
    
    


recursion([0]*len(coin),0)
for rs in sorted(result):
    #print(len(rs))
    if len(rs)==1:
        rs=str(rs)
        rs=rs.replace(",","")
    print(rs)
        