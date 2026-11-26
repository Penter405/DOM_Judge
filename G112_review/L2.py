array=[]
for _ in range(int(input())):
    d=int(input())
    array.append(d)
    array.sort()
    if len(array)%2==0:
        print((array[(len(array)-1)//2]+array[len(array)//2])//2)
    else:
        print(array[len(array)//2])
