while True:
    amount, devision=list(map(int,input().split()))
    print(amount,devision)
    if amount==0 and devision==0:
        break
    data=[]
    for _ in range(amount):
        now=int(input())
        devied=(abs(now)%abs(devision))
        if now<0:
            devied=-devied
        if now%2!=0:
            my_sort=-now
        else:
            my_sort=now
        
        data.append((devied,(now+1)%2,my_sort,now))

    data.sort()
    for index in range(len(data)):
        print(data[index][-1])
"""
15 3
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
0 0
"""