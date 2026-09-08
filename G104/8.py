import heapq
def get():
    data=input()
    member=set()
    queue=[]
    for rs in data.split():
        rs=rs.split(',')
        #print(rs)
        member.add(rs[0]);member.add(rs[1])
        heapq.heappush(queue,  (int(rs[2]),(rs[0],rs[1]))  )

    parent={}
    for rs in member:
        parent[rs]=rs

    def find(me):
        if parent[me]==me:
            return me
        return find(parent[me])
    def union(a,b):
        root_a=find(a)
        root_b=find(b)

        if root_a==root_b:
            return False

        parent[root_b]=root_a

        return True

    count=0
    result=0
    while queue:
        weight, node=heapq.heappop(queue)
        #print(weight)
        if count==len(member)-1:
            return result
        if union(*node):
            count+=1
            result+=weight
    return result


        
result=[]
for _ in range(int(input())):
    result.append(get())

for rs in result:
    print(rs)