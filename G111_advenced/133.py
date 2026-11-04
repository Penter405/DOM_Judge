def solve(x):
    if x%4!=0:
        return False
    if x%4==0 and x%100!=0:
        return True
    if x%100==0 and x%400!=0:
        return False
    if x%400==0:
        return True


res=[]
while True:
        try:
            x=int(input())
        except:
            break

        res.append(solve(x))



for i,rs in enumerate(res):
    if rs:
        print("a leap year")
    else:
        print("a normal year")