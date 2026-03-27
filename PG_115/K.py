n=int(input())
result=[]
for _ in range(n+1):
    #print(result)
    begin,end=list(map(int,input().split()))
    to_pop=[]
    for rs in range(len(result)):
        if result[rs][0]<=end and result[rs][1]>=begin:
            #print(f"match {begin} and {end} -> {result[rs]}")
            #print(begin,result[rs][0])
            begin=min(begin,result[rs][0])
            #print(begin)
            #print(end,result[rs][1])
            end=max(end,result[rs][1])
            #print(end)
            to_pop.append(rs)
    #print(to_pop)
    for rs in range(len(to_pop)-1,-1,-1):
        result.pop(to_pop[rs])
    result.append([begin,end])
#print(result)
result2=[]
while result:
    index=-1
    good_index=-1
    mins=-1
    for rs,pe in result:
        index+=1
        if mins==-1 or rs<mins:
            mins=rs
            good_index=index
    result2.append(result[good_index])
    result.pop(good_index)
print(result2)