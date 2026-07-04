answer=['one','two','three']
result=[]
def cheak():
    bot=input()
    if len(bot)==5:
        return 3
    mistaked=0
    for rs in range(3):
        if bot[rs]!=answer[0][rs]:
            mistaked+=1
    if mistaked<2:
        return 1
    return 2
        
for _ in range(int(input())):
    result.append(str(cheak()))
print("\n".join(result))
