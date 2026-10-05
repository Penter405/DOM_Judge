result=[]

def is_leap(a):
    if a%4!=0:
        return False
    if a%4==0 and a%100!=0:
        return True
    if a%100==0 and a%400!=0:
        return False
    if a%400==0:
        return True
for _ in range(int(input())):
    if is_leap(int(input())):
        result.append("a leap year")
    else:
        result.append("a normal year")


print("\n".join(result))