"""
1 -1
2 1
4 1+2
7 1+2+3

"""
from sys import stdin
d=stdin.read().split("\n")[:-1]
for integer in d:
    integer=int(integer)
    print((1+integer-1)*(integer-1)//2+1)