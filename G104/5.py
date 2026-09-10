"""

bin-> int to str

"""

result=[]
for _ in range(int(input())):
    data=int(input())
    buffer=0
    for rs in bin(data):
        if rs=='1':
            buffer+=1
    result.append(str(buffer))

print("\n".join(result))