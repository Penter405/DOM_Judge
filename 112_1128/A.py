from sys import stdin
d=stdin.read().split("\n")[:-1]
for line in d:
    array=eval(line)
    re=False
    if array[0]>array[-1]:
        re=True
    sed=sorted(array,reverse=re)
    for index in range(len(array)):
        if array[index]!=sed[index]:
            print("false")
            break
    else:
        print("true")