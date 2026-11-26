from bisect import bisect_left,bisect_right
past=[]
sizeof=int(input())
res=0
for i in list(map(int,input().split())):
    res+=len(past)-bisect_right(past,i)
    past.insert(bisect_left(past,i),i)
print(res)