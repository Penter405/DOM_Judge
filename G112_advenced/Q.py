nodes,swap=list(map(int,input().split()))
node=[0]+[n+1 for n in range(nodes)][::-1]
place=[0]+[len(node)-n-1 for n in range(nodes)]
res=[]
def add(value):
    while value<=nodes:
        bit[value]+=1
        value+=value&-value

def find(value):#bigger than you amounts
    res=0
    while value>0:
        res+=bit[value]
        value-=value&-value
    return res

for _ in range(swap):
    a,b=list(map(int,input().split()))
    bit=[0]*(nodes+1)
    aind=place[a]
    bind=place[b]
    node[aind],node[bind]=node[bind],node[aind]
    place[a],place[b]=place[b],place[a]
    buffer=0
    for index in range(1,nodes+1):
        buffer+=find(node[index])
        add(node[index])
    res.append(buffer)


for rs in res:
    print(rs)    