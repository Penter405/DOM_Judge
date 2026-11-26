for _ in range(int(input())):
    sizeof=int(input())
    d=input()
    same=0
    for i in range(sizeof):
        if i-2>=0 and d[i-2]==d[i]:
            same+=1
    print(sizeof-1-same)