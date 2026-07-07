def marge(a:list,b:list):
    result=[]
    pointer_a=0
    pointer_b=0
    #pointer means now seeing, change after see 
    while True:
        if pointer_a>=len(a) and pointer_b>=len(b):
            return result
        if pointer_a>=len(a):
            result.extend(b[pointer_b:])
        elif pointer_b>=len(b):
            result.extend(a[pointer_a:])
        elif a[pointer_a]<b[pointer_b]:
            result.append(a[pointer_a])
            pointer_a+=1
        else:
            result.append(b[pointer_b])
            pointer_b+=1
print(marge(list(map(int,input.split())),list(map(int,input.split()))))