"""
2d ?

"""

for _ in range(int(input())):
    product=[]
    for _ in range(int(input())):
        value,weight=list(map(int,input().split()))
        product.append((value,weight))
    guys=[]
    for _ in range(int(input())):
        guys.append(int(input()))
    large=max(guys)
    #only take once
    memo=[0]*(large+1)
    for value, weight in product:
        for index in range(large,weight-1,-1):
            now=index-weight
            if now<0:
                continue
            elif now==0:
                memo[index]=max(memo[index],value)
            elif memo[now]!=0:
                memo[index]=max(memo[index],memo[now]+value)
    premax=[]
    last=0
    for element in memo:
        premax.append(max(element,last))
        last=max(element,last)
    result=0
    for me in guys:
        result+=premax[me]
    print(result)
"""
2
3
72 17
44 23
31 24
1
26
6
64 26
85 22
52 4
99 18
39 13
54 9
4
23
20
20
26

"""