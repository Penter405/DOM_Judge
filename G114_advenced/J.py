from collections import Counter
rule=list(map(int,input().split()))
cr=dict(Counter(rule))
for _ in range(int(input())):
    d=list(map(int,input().split()))
    cd=dict(Counter(d))
    a=0;b=0
    for key in cd.keys():
        if key in cr:
            b+=min(cr[key],cd[key])
    for index in range(4):
        if rule[index]==d[index]:
            a+=1
    b-=a
    print("{}A{}B".format(a,b))
"""
1 2 3 4
4
1 1 4 5
1 2 4 3
1 1 4 4
4 3 2 1
"""