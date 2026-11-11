from sys import stdin
d=stdin.read().split("\n")[:-1]
for line in d:
    a,b=list(map(int,line.split()))
    print(a*b*2)