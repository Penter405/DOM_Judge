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
for _ in range(int(input())):
    res.append(solve(int(input())))

for rs in res:
    if rs:
        print("a leap year")
    else:
        print("a normal year")
