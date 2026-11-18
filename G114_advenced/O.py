from sys import stdin
def amount(string):
    if "0"<=string<="9":
        return int(string)
    if "A"<=string<="Z":
        return 10+ord(string)-65
    else:
        return 10+ord(string)-97+26
def legal(char):
    if "0"<=char<="9":
        return True
    if "A"<=char<="Z":
        return True
    if "a"<=char<="z":
        return True
    return False
"""
N based integer R
find min possible base
"""
for line in stdin.read().split("\n"):
    #if they switch line
    if line=="":
        continue
    line=[char for char in line if legal(char)]
    data=[]
    #-- if cheaked is empty
    if len(line)==0:
        continue
    for integer in line:
        data.append(amount(integer))
    large=max(data)
    #---
    go10=sum(data)
    for base in range(max(2,large+1),62+1):#range -> 1,  ->  go10% (1-1)  ->  devision zero  -> use max
        #---如果一個𝑁 進位制的數【𝑎𝑏𝑐】是(𝑁 − 1) 的倍數，則(𝑎 + 𝑏 + 𝑐) 也是(𝑁 − 1) 的倍數。
        if False:
            for char in data[::-1]:
                go10+=int(char)*nb
                nb*=base
            #--
        if go10%(base-1)==0:
            print(base)
            break
    else:
        print("such number is impossible!")
"""
3
5
A
2727
Zz
-   A

"""