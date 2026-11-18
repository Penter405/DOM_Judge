


def search(target,table):
    left=0
    right=len(table)-1
    while left<=right:
        mid=(left+right)//2#near left
        if table[mid]==target:
            return mid+1
        elif table[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return 0
given, find=list(map(int,input().split()))
got=list(map(int,input().split()))
do=list(map(int,input().split()))
for guy in do:
    print(search(guy,got))
"""
5 5
1 3 4 7 9
3 1 9 7 -2
"""