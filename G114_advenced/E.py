import sys
#import math
def cheak(now):
    for base in 2,3,5:
        #goal=math.log(now,2)
        while now%base==0:
            now//=base
    return now==1

for line in sys.stdin.read().split("\n")[:-1]:
    print(cheak(int(line)))