#greedy
from sys import stdin
d=stdin.read().split("\n")[:-1]
for line in d:
    a,b,a2,b2,distance=list(map(int,line.split(",")))
    required=max(abs(a2-a),abs(b2-b))
    if (required==0 and distance==1):
        print('false')
    else:
        print(str( required<=distance  ).lower())


exit()
import sys
for line in sys.stdin:
 if line.strip():
  sx,sy,fx,fy,t=map(int,line.split(','))
  d=max(abs(sx-fx),abs(sy-fy))
  print(str(d<=t and not(d==0 and t==1)).lower())
