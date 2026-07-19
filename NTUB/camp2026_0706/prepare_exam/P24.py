import math
#print(math.lcm(15,20))

a=list(map(int,input().split(',')))
b=list(map(int,input().split(',')))

under=math.lcm(a[1],b[1])
a[0]*=under//a[1]
b[0]*=under//b[1]
new=[a[0]+b[0],under]
take=math.gcd(*new)
new[0]//=take
new[1]//=take
print("{}/{}".format(*new))