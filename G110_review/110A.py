from sys import stdin
d=stdin.read().split('\n')
for line in d:
    if line=='':
        continue
    a,b=list(map(int,line.split()))
    print(a*4+b*6)