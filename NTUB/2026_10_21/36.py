from collections import Counter
from math import factorial
"""
ban
cd
cr
o(1)


permutaiton=(all!/a!*b! )*1
"""
s=input()
d=dict(Counter(s))

a=d.get("d",0)
b=d.get("r",0)
if a==0 or b==0:
    print(1)
else:
    print(factorial(a+b)//(factorial(a)*factorial(b)))