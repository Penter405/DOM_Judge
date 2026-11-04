a=eval(input())
a=list(zip(*a))
b=[]
for rs in a:
    b.append(list(rs[::-1]))
print(str(b).replace(" ",""))