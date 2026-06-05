useless=input()
coin=list(map(int,input().split()))
result=set()
goal=int(input())
ever=set()
def recursion(my_list,less):
    #print(my_list)
    if tuple(my_list) in ever:
        return 0
    ever.add(tuple(my_list))
    if less==0:
        result.add(tuple(my_list))
    if less<0:
        return 0
    for rs in range(len(coin)):
        my_list2=my_list.copy()
        my_list2[rs]+=1
        recursion(my_list2,less-coin[rs])

recursion([0]*len(coin),goal)
for rs in sorted(result):
    if len(rs)==1:
        rs=str(rs)
        rs=rs.replace(" ","")
        rs=rs.replace(",","")
        print(rs)
    else:
        rs=str(rs)
        rs=rs.replace(" ","")
        print(rs)