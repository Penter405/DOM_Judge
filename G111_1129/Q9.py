import bisect
array,target=input().split()
array=list(map(int,array.split(",")))
target=int(target)
print(bisect.bisect_left(array,target))
