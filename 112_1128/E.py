from collections import deque,defaultdict
from sys import stdin
d=stdin.read().split("\n")[:-1]
for line in d:
    res=defaultdict(int)
    line=line[::-1]
    line=line.split(",",1)
    line[0]=line[0][::-1]
    line[1]=line[1][::-1]
    integer,array=line
    integer=int(integer)
    array=eval(array)
    if array[0]==max(array):
        print(array[0])
        continue
    que=deque(array)
    while True:
        a,b=que[0],que[1]
        que.popleft()
        if a<b:
            a,b=b,a
        que[0]=a
        que.append(b)
        res[a]+=1
        if res[a]==integer:
            print(a)
            break

        

