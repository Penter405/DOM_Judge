"""
必須依照數字與字母的
順序搭建，否則整座階梯會立刻崩塌

        |
135 ->  |
        |


246 ->  ----


"""


d=int(input())
letter=-1
integer=0
k=0
for rs in range(1,d+1):
    if rs%2!=0:
        k+=1
        integer+=1
        for _ in range(d):
            print("_"*((k-1)*d)+str(integer))
    else:
        letter+=1
        print("_"*((k-1)*d)+chr(97+letter)*(d+1))
    