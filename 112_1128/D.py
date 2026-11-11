#greedy
from sys import stdin
d=stdin.read().split("\n")[:-1]
for line in d:
    a,b,a2,b2,distance=list(map(int,line.split(",")))
    required=max(abs(a2-a),abs(b2-b))
    print(str( required<=distance  ).lower())
