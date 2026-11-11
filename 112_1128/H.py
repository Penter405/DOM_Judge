#o(n**2)
from sys import stdin
d=stdin.read().split("\n")[:-1]
for line in d:
    
    array=list(map(int,line.split(",")))
    size=len(array)
    dp=[1]*size
    res=size
    #me and child relation ship, take all child, take child -1 take..child 1 with me(1)
    for index in range(1,size):
        past=index-1
        if array[index]>array[past]:
            dp[index]+=dp[past]
    print(sum(dp))
    
"""
1,3,5,4,4,6
1,2,3,4,5
"""