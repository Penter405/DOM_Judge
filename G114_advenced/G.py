from sys import stdin
def cheak(n:int):
    stringout=[]
    result=0
    while n:
        if n%2!=0:
            n-=1
            result+=1
        else:
            break
        n//=2

    return result

for line in stdin.read().split("\n")[:-2]:
    print(cheak(int(line)))