n=int(input())
last=None
keep=0
result=[]
ever=set()
for rs in input():
    if last==None:
        last=rs
        keep+=1
    else:
        if last==rs:
            keep+=1
        else:
            last=rs
            keep=1
    if keep>n:
        if rs not in ever:
            result.append(rs)
            ever.add(rs)
        
if len(result)==0:
    print("NONE")
else:
    print("".join(sorted(result)))
"""
O    給定一個整數 n 和一個只包含小寫英文字母的字串 s。
O    請找出字串中哪些字母曾經「連續出現超過 n 次」。
X(O)    若同一個字母在字串中出現多段連續區間，只要其中任一段連續出現次數超過n，就算符合條件。
O   最後請將符合條件的字母依照字母順序輸出。
O    若沒有任何字母符合條件，請輸出 NONE。
"""