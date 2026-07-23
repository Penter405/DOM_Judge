result=0
words=[]
for rs in input():
    try:
        rs=int(rs)
        result+=rs
    except:
        #it word
        words.append(rs.upper())
print(f"{''.join(words[::-1])} {result}")