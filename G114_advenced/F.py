from sys import stdin
"""
binary -> can be %2 -> 

"""
def cheak(n:int):
    stringout=[]
    result=0
    while n:
        if n%2!=0:
            n-=1
            result+=1
            stringout.append("1")
        else:
            stringout.append("0")
        n//=2

    return ["".join(stringout[::-1]),result]

for line in stdin.read().split("\n")[:-2]:
    print("The parity of {} is {} (mod 2).".format(*cheak(int(line))))