result=""
def get(x):
    global result
    for rs in x:
        bot=ord(rs)
        if (bot>=65 and bot<=90) or (bot>=97 and bot<=122):
            result+=rs

get(input())
print(result)