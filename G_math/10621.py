def cheak(string):
    total=0
    for index in range(16):
        time=1
        if index%2==0:
            time=2
        now=int(string[index])*time
        now=now//10+now%10
        total+=now
    return total%10==0
for _ in range(int(input())):
    if cheak(input()):
        print("T")
    else:
        print("F")
