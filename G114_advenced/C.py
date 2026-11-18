def prime(n):
    if n%4!=0:
        return False
    if n%4==0 and n%100!=0:
        return True
    if n%100==0 and n%400!=0:
        return False
    if n%400==0:
        return True

print(prime(int(input())+1911))