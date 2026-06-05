useless=input()
coin=list(map(int,input().split()))
result=set()
goal=int(input())
def recursion(my_list,less):
    #print(my_list)
    if less==0:
        result.add(str(tuple(my_list)))
    if less<0:
        return 0
    for rs in range(len(coin)):
        my_list2=my_list.copy()
        my_list2[rs]+=1
        recursion(my_list2,less-coin[rs])

recursion([0]*len(coin),goal)
for rs in sorted(result):
    rs=rs.replace(" ","")
    print(rs)