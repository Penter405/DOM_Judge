result=[]
def what(a):
    if len(a)==5:
        return 3
    data="one"
    count_bad=0
    for rs in range(3):
        if data[rs]!=a[rs]:
            count_bad+=1

    if count_bad>1:
        return 2
    return 1

for _ in range(int(input())):
    result.append(str(what(input())))

print("\n".join(result))